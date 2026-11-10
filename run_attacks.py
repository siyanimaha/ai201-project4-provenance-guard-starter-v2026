
#!/usr/bin/env python3
"""
Run the attack set against your Provenance Guard service.

Examples:

python run_attacks.py --set attack_set/attack_set
python run_attacks.py --set attack_set/attack_set --label before
python run_attacks.py --set attack_set/attack_set --label after
python run_attacks.py --set attack_set/attack_set --id RQ07 --show
python run_attacks.py --set attack_set/attack_set --id RQ07
python run_attacks.py --flood 15
"""

import argparse
import csv
import datetime as dt
import json
import sys
from pathlib import Path

import config


for stream in (sys.stdout, sys.stderr):
    try:
        stream.reconfigure(errors="replace")
    except (AttributeError, ValueError):
        pass


DEFAULT_URL = f"http://{config.HOST}:{config.PORT}"
CURL_TOO_LONG = 2000

FLOOD_TEXT = (
    "This is an ordinary submission, sent over and over from the same "
    "account to find out where the rate limit sits. Nothing about the "
    "text matters here."
)


# --------------------------------------------------
# LOAD ATTACKS
# --------------------------------------------------

def load_attacks(folder):
    attacks = []
    problems = []

    text_file = folder / "attacks.csv"

    if text_file.exists():
        with text_file.open(encoding="utf-8") as f:
            for n, row in enumerate(csv.DictReader(f), 2):
                try:
                    attacks.append({
                        "id": row["id"],
                        "family": row["family"],
                        "targets": row["targets"],
                        "body": {
                            "text": row["text"],
                            "creator_id": f"attacker_{row['id']}",
                        },
                    })
                except (KeyError, TypeError) as exc:
                    problems.append(
                        f"attacks.csv line {n}: {exc}"
                    )

    request_file = folder / "attacks_malformed_requests.csv"

    if request_file.exists():
        with request_file.open(encoding="utf-8") as f:
            for n, row in enumerate(csv.DictReader(f), 2):
                try:
                    attack = {
                        "id": row["id"],
                        "family": row["family"],
                        "targets": row["targets"],
                    }

                    send_as = (
                        row.get("send_as") or "json"
                    ).strip().lower()

                    if send_as == "raw":
                        attack["raw"] = row["raw_body"]
                        attack["content_type"] = (
                            row.get("content_type")
                            or "application/json"
                        )
                    else:
                        attack["body"] = json.loads(
                            row["raw_body"]
                        )

                    attacks.append(attack)

                except (
                    KeyError,
                    TypeError,
                    json.JSONDecodeError,
                ) as exc:
                    problems.append(
                        f"attacks_malformed_requests.csv "
                        f"line {n}: {exc}"
                    )

    return attacks, problems


# --------------------------------------------------
# SEND ATTACK
# --------------------------------------------------

def send(url, attack, timeout):
    import requests

    try:
        if "raw" in attack:
            response = requests.post(
                f"{url}/submit",
                data=attack["raw"].encode("utf-8"),
                headers={
                    "Content-Type": attack["content_type"]
                },
                timeout=timeout,
            )
        else:
            response = requests.post(
                f"{url}/submit",
                json=attack["body"],
                timeout=timeout,
            )

    except Exception as exc:
        return None, None, (
            f"{type(exc).__name__}: {exc}"
        )

    try:
        return response.status_code, response.json(), None
    except ValueError:
        return (
            response.status_code,
            None,
            f"response wasn't JSON: {response.text[:200]}",
        )


# --------------------------------------------------
# RATE LIMIT WARNING
# --------------------------------------------------

def warn_about_rate_limits(attacks, health):
    needs_limits = sorted({
        a["family"]
        for a in attacks
        if "flood" in a["family"]
    })

    if not needs_limits:
        return

    if health.get("rate_limiting"):
        return

    print("\n" + "!" * 60, file=sys.stderr)
    print(
        "WARNING: Rate limiting is OFF.",
        file=sys.stderr,
    )
    print(
        f"Flood families: {', '.join(needs_limits)}",
        file=sys.stderr,
    )
    print(
        "Turn on rate limiting before testing floods.",
        file=sys.stderr,
    )
    print("!" * 60 + "\n", file=sys.stderr)


# --------------------------------------------------
# AUTOMATIC VERDICTS
# --------------------------------------------------

def auto_verdict(status, payload, error):
    if error and "ConnectionError" in error:
        return "BROKE", "the service stopped responding"

    if error:
        return "BROKE", error[:60]

    if status is None:
        return "BROKE", "no response"

    if status >= 500:
        return "BROKE", f"{status} — unhandled error"

    return "", ""


# --------------------------------------------------
# SELECT ATTACKS
# --------------------------------------------------

def select_attacks(attacks, args):
    if args.attack_id:
        wanted = args.attack_id.strip().lower()

        picked = [
            a for a in attacks
            if a["id"].lower() == wanted
        ]

        if not picked:
            known = [a["id"] for a in attacks]

            return [], (
                f"No attack with ID '{args.attack_id}'.\n"
                f"Available examples: {', '.join(known[:5])}"
            )

        return picked, None

    if args.one_per_family:
        first = {}

        for attack in attacks:
            first.setdefault(
                attack["family"],
                attack,
            )

        return list(first.values()), None

    if args.family:
        picked = [
            a for a in attacks
            if a["family"] == args.family
        ]

        if not picked:
            families = sorted({
                a["family"] for a in attacks
            })

            return [], (
                f"Unknown family: {args.family}\n"
                f"Available: {', '.join(families)}"
            )

        return picked, None

    return attacks, None


# --------------------------------------------------
# GENERATE CURL COMMANDS
# --------------------------------------------------

def curl_commands(url, attack):
    if "raw" in attack:
        body = attack["raw"]
        content_type = attack["content_type"]
    else:
        body = json.dumps(attack["body"])
        content_type = "application/json"

    bash_body = body.replace("'", "'\\''")

    bash = (
        f"curl -X POST {url}/submit \\\n"
        f'  -H "Content-Type: {content_type}" \\\n'
        f"  -d '{bash_body}'"
    )

    windows_body = (
        body.replace('"', '\\"')
        .replace("'", "''")
    )

    windows = (
        f"curl.exe -X POST {url}/submit "
        f'-H "Content-Type: {content_type}" '
        f"-d '{windows_body}'"
    )

    return bash, windows


# --------------------------------------------------
# SHOW ATTACKS WITHOUT SENDING
# FIXES RQ07 JSON LIST CRASH
# --------------------------------------------------

def show_attacks(attacks, url):
    for attack in attacks:
        print("=" * 70)
        print(
            f"{attack['id']}  ·  {attack['family']}"
        )
        print("=" * 70)

        print(
            f"\nTargeting: {attack['targets']}\n"
        )

        if "raw" in attack:
            print(
                f"Sent raw, claiming "
                f"{attack['content_type']}:\n"
            )

            print(
                attack["raw"]
                if attack["raw"]
                else "(an empty body)"
            )

        else:
            body = attack.get("body")

            # Only dictionaries can contain a text field.
            # RQ07 uses a JSON list.
            if isinstance(body, dict) and "text" in body:
                print(body["text"])

                creator_id = body.get(
                    "creator_id",
                    "unknown",
                )

                print(
                    f"\n(submits as creator_id "
                    f"`{creator_id}`)"
                )

            else:
                print(
                    "No text field — the body itself "
                    "is the attack:\n"
                )

                print(
                    json.dumps(
                        body,
                        indent=2,
                        ensure_ascii=False,
                    )
                )

        bash, windows = curl_commands(
            url,
            attack,
        )

        if len(bash) > CURL_TOO_LONG:
            print(
                f"\nThe curl command is "
                f"{len(bash):,} characters long."
            )

            print(
                "\nSend this attack using:\n"
                "python run_attacks.py "
                "--set attack_set/attack_set "
                f"--id {attack['id']}"
            )

            continue

        print(
            "\n--- curl "
            "--------------------------------------------------\n"
        )
        print(bash)

        print(
            "\n--- PowerShell "
            "--------------------------------------------\n"
        )
        print(windows)
        print()

    print(
        f"{len(attacks)} attack(s) shown. "
        "Nothing was sent and no report was written."
    )


# --------------------------------------------------
# CHECK REQUESTS PACKAGE
# --------------------------------------------------

def require_requests():
    try:
        import requests
    except ImportError:
        print(
            "The requests package is missing.\n"
            "Run: pip install -r requirements.txt",
            file=sys.stderr,
        )
        sys.exit(1)


# --------------------------------------------------
# FLOOD TEST
# --------------------------------------------------

def run_flood(args):
    import requests

    print(
        f"{args.flood} submissions as "
        f"'{args.creator}' against {args.url}"
    )

    print(
        "The first request may be slow "
        "while the model loads.\n"
    )

    codes = []

    for i in range(1, args.flood + 1):
        try:
            response = requests.post(
                f"{args.url}/submit",
                json={
                    "text": FLOOD_TEXT,
                    "creator_id": args.creator,
                },
                timeout=args.timeout,
            )

            codes.append(
                str(response.status_code)
            )

        except Exception as exc:
            codes.append(
                type(exc).__name__
            )

        print(
            f"  [{i:>2}/{args.flood}] "
            f"{codes[-1]}"
        )

    run = " ".join(codes)

    limited = sum(
        1 for code in codes
        if code == "429"
    )

    print("\n" + "=" * 60)
    print(run)
    print("=" * 60)

    if limited:
        print(
            f"\n{limited} of {len(codes)} "
            "were rate limited."
        )
    else:
        print(
            "\nNo 429 responses. Check "
            "whether rate limiting is enabled."
        )

    config.RESULTS_DIR.mkdir(
        exist_ok=True
    )

    stamp = dt.datetime.now().strftime(
        "%Y-%m-%d_%H%M"
    )

    path = (
        config.RESULTS_DIR
        / f"flood_{stamp}.md"
    )

    path.write_text(
        "# Rate limit check\n\n"
        "- Produced by: `run_attacks.py::run_flood`\n"
        f"- {len(codes)} submissions as "
        f"`{args.creator}`\n"
        f"- Rate limited: **{limited}**\n\n"
        f"```\n{run}\n```\n",
        encoding="utf-8",
    )

    print(
        f"\nWrote "
        f"{path.relative_to(config.ROOT)}"
    )


# --------------------------------------------------
# MAIN
# --------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=(
            argparse.RawDescriptionHelpFormatter
        ),
    )

    parser.add_argument(
        "--set",
        dest="folder",
        help="Folder holding attacks.csv",
    )

    parser.add_argument(
        "--flood",
        type=int,
        metavar="N",
        help="Send N submissions from one creator",
    )

    parser.add_argument(
        "--creator",
        default="flood_tester",
    )

    parser.add_argument(
        "--url",
        default=DEFAULT_URL,
    )

    parser.add_argument(
        "--label",
        default="",
    )

    parser.add_argument(
        "--timeout",
        type=float,
        default=90.0,
    )

    parser.add_argument(
        "--family",
    )

    parser.add_argument(
        "--id",
        dest="attack_id",
        metavar="ID",
    )

    parser.add_argument(
        "--one-per-family",
        action="store_true",
    )

    parser.add_argument(
        "--show",
        action="store_true",
    )

    args = parser.parse_args()

    if args.flood:
        require_requests()
        run_flood(args)
        return

    if not args.folder:
        print(
            "Give an attack set using --set.\n"
            "Example:\n"
            "python run_attacks.py "
            "--set attack_set/attack_set",
            file=sys.stderr,
        )

        sys.exit(1)

    folder = Path(args.folder)

    attacks, problems = load_attacks(folder)

    if problems:
        print(
            f"{len(problems)} attack row(s) "
            "could not be parsed:",
            file=sys.stderr,
        )

        for problem in problems:
            print(
                f"  - {problem}",
                file=sys.stderr,
            )

    if not attacks:
        print(
            f"No attacks found in {folder}.",
            file=sys.stderr,
        )

        sys.exit(1)

    attacks, complaint = select_attacks(
        attacks,
        args,
    )

    if complaint:
        print(
            complaint,
            file=sys.stderr,
        )

        sys.exit(1)

    if args.show:
        show_attacks(
            attacks,
            args.url,
        )
        return

    require_requests()

    import requests

    try:
        health = requests.get(
            f"{args.url}/health",
            timeout=5,
        ).json()

    except Exception:
        print(
            f"Nothing answering at {args.url}.\n"
            "Start your service first:\n"
            "python app.py",
            file=sys.stderr,
        )

        sys.exit(1)

    warn_about_rate_limits(
        attacks,
        health,
    )

    print(
        f"{len(attacks)} attacks against "
        f"{args.url}"
    )

    print(
        "Signal one runs a model. "
        "The first request may be slow.\n"
    )

    rows = []

    for i, attack in enumerate(attacks, 1):
        status, payload, error = send(
            args.url,
            attack,
            args.timeout,
        )

        verdict, note = auto_verdict(
            status,
            payload,
            error,
        )

        # Responses can also contain unexpected
        # JSON types, so normalize safely.
        if not isinstance(payload, dict):
            payload = {}

        attack_body = attack.get("body")

        if isinstance(attack_body, dict):
            creator_id = attack_body.get(
                "creator_id"
            )
        else:
            creator_id = None

        row = {
            "id": attack["id"],
            "family": attack["family"],
            "targets": attack["targets"],
            "status": status,
            "content_id": payload.get(
                "content_id"
            ),
            "creator_id": creator_id,
            "guess": payload.get("guess"),
            "confidence": payload.get(
                "confidence"
            ),
            "model_score": payload.get(
                "model_score"
            ),
            "style_score": payload.get(
                "style_score"
            ),
            "label": payload.get("label"),
            "error": error,
            "verdict": verdict,
            "note": note,
        }

        rows.append(row)

        mark = verdict or "?"

        guess = payload.get("guess") or "—"

        print(
            f"  [{i:>2}/{len(attacks)}] "
            f"{attack['id']:<6} "
            f"{attack['family']:<17} "
            f"{str(status):<5} "
            f"{str(guess):<8} "
            f"{mark}"
        )

    write_report(rows, args)


# --------------------------------------------------
# WRITE RESULTS REPORT
# --------------------------------------------------

def write_report(rows, args):
    config.RESULTS_DIR.mkdir(
        exist_ok=True
    )

    stamp = dt.datetime.now().strftime(
        "%Y-%m-%d_%H%M"
    )

    label = (
        f"_{args.label}"
        if args.label
        else ""
    )

    path = (
        config.RESULTS_DIR
        / f"attack_run_{stamp}{label}.md"
    )

    broke = sum(
        1 for row in rows
        if row["verdict"] == "BROKE"
    )

    undecided = sum(
        1 for row in rows
        if not row["verdict"]
    )

    heading = (
        f"# Attack run — {args.label}"
        if args.label
        else "# Attack run"
    )

    lines = [
        heading,
        "",
        "- Produced by: `run_attacks.py::main`",
        "- Service: `app.py::submit`",
        f"- {len(rows)} attacks",
        f"- Auto-marked BROKE: **{broke}**",
        f"- Left for you to judge: **{undecided}**",
        "",
        "Read the targets column and decide "
        "whether each attack HELD or BROKE.",
        "",
        "| ID | Family | Targeting | Status | "
        "Content ID | Guess | Score | Verdict |",
        "|---|---|---|---|---|---|---|---|",
    ]

    for row in rows:
        score = row["confidence"]

        if isinstance(score, (int, float)):
            score_text = f"{score:.3f}"
        else:
            score_text = "—"

        targets = row["targets"].replace(
            "|",
            "\\|",
        )

        status_text = (
            str(row["status"])
            if row["status"] is not None
            else "—"
        )

        lines.append(
            f"| {row['id']} "
            f"| {row['family']} "
            f"| {targets} "
            f"| {status_text} "
            f"| `{row['content_id'] or '—'}` "
            f"| {row['guess'] or '—'} "
            f"| {score_text} "
            f"| {row['verdict'] or ''} |"
        )

    lines.extend([
        "",
        "---",
        "",
        "## By family",
        "",
        "| Family | Attacks | Auto-BROKE | "
        "Left to judge |",
        "|---|---|---|---|",
    ])

    families = {}

    for row in rows:
        families.setdefault(
            row["family"],
            [],
        ).append(row)

    for family, items in sorted(
        families.items()
    ):
        auto = sum(
            1 for row in items
            if row["verdict"] == "BROKE"
        )

        lines.append(
            f"| `{family}` "
            f"| {len(items)} "
            f"| {auto} "
            f"| {len(items) - auto} |"
        )

    lines.extend([
        "",
        "The false_positive family tests "
        "human writing that may look AI-generated.",
        "",
        "---",
        "",
        "## What came back",
        "",
    ])

    for row in rows:
        lines.extend([
            f"### {row['id']} — "
            f"`{row['family']}`",
            "",
            f"*Targeting:* {row['targets']}",
            "",
            "```json",
            json.dumps(
                {
                    k: v
                    for k, v in row.items()
                    if k not in (
                        "targets",
                        "family",
                        "note",
                    )
                },
                indent=2,
            ),
            "```",
            "",
        ])

    path.write_text(
        "\n".join(lines),
        encoding="utf-8",
    )

    print("\n" + "=" * 60)

    print(
        f"Wrote "
        f"{path.relative_to(config.ROOT)}"
    )

    print(
        f"  auto-marked BROKE: {broke}"
    )

    print(
        f"  left for you:      {undecided}"
    )

    print("=" * 60)

    print(
        "\nNow pull your audit log "
        "and paste ten entries into your README."
    )

    print(
        '\n  curl "http://127.0.0.1:5000/'
        'log?limit=200" > '
        'results/audit_extract.json'
    )


if __name__ == "__main__":
    main()
