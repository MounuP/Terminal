import json, re
from collections import Counter
from pathlib import Path

def test_report_exists():
    """The agent produced a report file."""
    assert Path("/app/report.json").exists(), "report.json was not created"


def test_report_valid_json():
    """Verifies the instruction.md criteria: the report must be a valid JSON object."""
    with open("/app/report.json") as f:
        report = json.load(f)

    assert isinstance(report, dict), "report.json must contain a JSON object"


def test_report_correct_values():
    """Verifies the instruction.md criteria: total_requests, unique_ips, and top_path are correctly calculated from /app/access.log."""
paths, ips, total = Counter(), set(), 0

    with open("/app/access.log") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            total += 1
            ips.add(line.split()[0])

            match = re.search(r'"(?:GET|POST|PUT|DELETE|HEAD|PATCH) (\S+) ', line)
            if match:
                paths[match.group(1)] += 1

    expected = {
        "total_requests": total,
        "unique_ips": len(ips),
        "top_path": paths.most_common(1)[0][0],
    }

    with open("/app/report.json") as f:
        report = json.load(f)

    assert report == expected, "report values do not match access.log analysis"
