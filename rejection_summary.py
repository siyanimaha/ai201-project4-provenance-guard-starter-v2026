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
