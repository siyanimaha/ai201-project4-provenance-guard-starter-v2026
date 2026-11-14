from collections import Counter
from audit import read_entries


def summarize_rejections():
    entries = read_entries()
    rejected = [
        entry for entry in entries
        if entry.get("event") == "rejected"
    ]

    reasons = Counter(
        entry.get("reason", "unknown")
        for entry in rejected
    )

    return {
        "total_rejected": len(rejected),
        "reasons": dict(reasons)
    }


if __name__ == "__main__":
    summary = summarize_rejections()
    print("Rejected Request Summary")
    print("Total rejected:", summary["total_rejected"])

    for reason, count in summary["reasons"].items():
        print(f"{reason}: {count}")

def run_with_logging():
    import json
    import time
    from datetime import datetime, timezone
    from pathlib import Path

    log_path = Path("logs/capstone_runs.jsonl")
    log_path.parent.mkdir(parents=True, exist_ok=True)

    start = time.perf_counter()
    record = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "status": "success"
    }

    try:
        summary = summarize_rejections()
        record["total_rejected"] = summary["total_rejected"]
        record["reasons"] = summary["reasons"]
        return summary
    except Exception as error:
        record["status"] = "failure"
        record["error"] = str(error)
        raise
    finally:
        record["runtime_ms"] = round(
            (time.perf_counter() - start) * 1000, 3
        )
        with log_path.open("a", encoding="utf-8") as file:
            file.write(json.dumps(record) + "\n")
