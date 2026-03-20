"""
check-pekeliling.py — Check for new Pekeliling Bendahari releases.

Scrapes the Jabatan Bendahari website looking for pekeliling
documents that aren't already tracked in the repo.

Usage:
    python scripts/check-pekeliling.py
"""

import re
from datetime import datetime
from pathlib import Path

import requests
from bs4 import BeautifulSoup

BENDAHARI_URL = "https://bendahari.ukm.my"
OUTPUT_DIR = Path(__file__).parent / "output"

# Known pekeliling already in the repo (update this list as you add new ones)
KNOWN_PEKELILING = [
    "Pekeliling Bendahari Bil. 8/2022",
    "Pekeliling Bendahari Bil. 4/2025",
]

HEADERS = {
    "User-Agent": "UKM-Event-Management-Bot/1.0 (educational repo maintenance)"
}


def fetch_bendahari_page():
    """Fetch the Bendahari main page."""
    try:
        resp = requests.get(BENDAHARI_URL, headers=HEADERS, timeout=15)
        resp.raise_for_status()
        return resp.text
    except requests.RequestException as e:
        print(f"❌ Failed to fetch Bendahari page: {e}")
        return None


def find_pekeliling_links(html):
    """Extract pekeliling references from the page."""
    soup = BeautifulSoup(html, "html.parser")
    found = []

    # Look for links and text containing "pekeliling"
    for tag in soup.find_all(["a", "p", "li", "td", "span", "div"]):
        text = tag.get_text(strip=True).lower()
        if "pekeliling" in text and "bendahari" in text:
            link = tag.get("href", "") if tag.name == "a" else ""
            original_text = tag.get_text(strip=True)
            found.append({"text": original_text, "link": link})

    # Also search for PDF links that might be pekeliling
    for a in soup.find_all("a", href=True):
        href = a["href"].lower()
        if "pekeliling" in href and href.endswith(".pdf"):
            found.append({"text": a.get_text(strip=True), "link": a["href"]})

    # Deduplicate by text
    seen = set()
    unique = []
    for item in found:
        if item["text"] not in seen:
            seen.add(item["text"])
            unique.append(item)

    return unique


def check_for_new(found_items):
    """Check if any found pekeliling are not in our known list."""
    new_items = []
    for item in found_items:
        is_known = False
        for known in KNOWN_PEKELILING:
            if known.lower() in item["text"].lower():
                is_known = True
                break
        if not is_known:
            new_items.append(item)
    return new_items


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().isoformat()

    print(f"=== Pekeliling Checker — {timestamp} ===\n")
    print(f"Known pekeliling in repo: {len(KNOWN_PEKELILING)}")
    for k in KNOWN_PEKELILING:
        print(f"  ✅ {k}")

    print(f"\nFetching {BENDAHARI_URL}...")
    html = fetch_bendahari_page()
    if html is None:
        return 1

    found = find_pekeliling_links(html)
    print(f"Found {len(found)} pekeliling reference(s) on page.\n")

    new_items = check_for_new(found)

    if new_items:
        print(f"🔔 {len(new_items)} potentially NEW pekeliling found:\n")
        for item in new_items:
            print(f"  📄 {item['text']}")
            if item["link"]:
                print(f"     Link: {item['link']}")
            print()

        # Save report
        report_path = OUTPUT_DIR / "new_pekeliling.txt"
        with open(report_path, "w") as f:
            f.write(f"Pekeliling Check — {timestamp}\n")
            f.write(f"{'=' * 50}\n\n")
            for item in new_items:
                f.write(f"Title: {item['text']}\n")
                f.write(f"Link: {item['link'] or 'N/A'}\n\n")
        print(f"Report saved to: {report_path}")
    else:
        print("✅ No new pekeliling detected. Repo is up to date.")

    return len(new_items)


if __name__ == "__main__":
    exit(0 if main() == 0 else 1)
