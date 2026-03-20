"""
scrape-public.py — Scrape public UKM pages for changes.

Checks key public-facing UKM pages and saves their content
for diffing against previous runs. Outputs to scripts/output/.

Usage:
    python scripts/scrape-public.py
"""

import os
import hashlib
import json
from datetime import datetime
from pathlib import Path

import requests
from bs4 import BeautifulSoup

# Pages to monitor
TARGETS = [
    {
        "name": "bendahari-main",
        "url": "https://bendahari.ukm.my",
        "description": "Jabatan Bendahari main page — check for new pekeliling links",
    },
    {
        "name": "ivi-facilities",
        "url": "https://ivi.ukm.my/facilities/",
        "description": "IVI/AST facilities page — check for venue/contact changes",
    },
    {
        "name": "ep-ukm",
        "url": "https://ukmperolehan.ukm.my/",
        "description": "eP@UKM procurement portal — check for system changes",
    },
]

OUTPUT_DIR = Path(__file__).parent / "output"
HISTORY_FILE = OUTPUT_DIR / "scrape_history.json"

HEADERS = {
    "User-Agent": "UKM-Event-Management-Bot/1.0 (educational repo maintenance)"
}


def ensure_output_dir():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def load_history():
    if HISTORY_FILE.exists():
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    return {}


def save_history(history):
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)


def fetch_page(url):
    """Fetch a page and return its text content."""
    try:
        resp = requests.get(url, headers=HEADERS, timeout=15)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")

        # Remove script and style elements
        for tag in soup(["script", "style", "nav", "footer"]):
            tag.decompose()

        text = soup.get_text(separator="\n", strip=True)
        return text
    except requests.RequestException as e:
        print(f"  ❌ Failed to fetch {url}: {e}")
        return None


def content_hash(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def main():
    ensure_output_dir()
    history = load_history()
    changes = []
    timestamp = datetime.now().isoformat()

    print(f"=== UKM Public Page Scraper — {timestamp} ===\n")

    for target in TARGETS:
        name = target["name"]
        url = target["url"]
        print(f"Checking: {name} ({url})")

        text = fetch_page(url)
        if text is None:
            continue

        # Save current content
        output_file = OUTPUT_DIR / f"{name}.txt"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(text)

        # Compare with previous
        current_hash = content_hash(text)
        previous_hash = history.get(name, {}).get("hash", "")

        if current_hash != previous_hash:
            if previous_hash:
                print(f"  ⚠️  CHANGE DETECTED — content differs from last run")
                changes.append(
                    {
                        "name": name,
                        "url": url,
                        "description": target["description"],
                        "previous_check": history.get(name, {}).get("timestamp", "never"),
                    }
                )
            else:
                print(f"  📝 First run — baseline saved")
        else:
            print(f"  ✅ No changes")

        history[name] = {"hash": current_hash, "timestamp": timestamp, "url": url}

    save_history(history)

    # Summary
    print(f"\n=== Summary ===")
    if changes:
        print(f"🔔 {len(changes)} page(s) changed:")
        for c in changes:
            print(f"  - {c['name']}: {c['description']}")
            print(f"    Last checked: {c['previous_check']}")
            print(f"    Review: scripts/output/{c['name']}.txt")

        # Save changes report
        report_file = OUTPUT_DIR / "changes_report.json"
        with open(report_file, "w") as f:
            json.dump({"timestamp": timestamp, "changes": changes}, f, indent=2)
        print(f"\nChanges report saved to: {report_file}")
    else:
        print("✅ No changes detected on any monitored page.")

    return len(changes)


if __name__ == "__main__":
    exit(0 if main() == 0 else 1)
