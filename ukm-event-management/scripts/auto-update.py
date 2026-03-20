"""
auto-update.py — Orchestrator for autonomous repo updates.

Runs all scrapers, checks for changes, and auto-commits if
changes are detected. Designed to be called by GitHub Actions
or manually.

Usage:
    python scripts/auto-update.py

Environment variables (optional, from .env):
    UKM_EWARGA_USER — ewarga username (for SMPR checks, future use)
    UKM_EWARGA_PASS — ewarga password (for SMPR checks, future use)
"""

import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass  # dotenv not required if env vars are set directly

REPO_ROOT = Path(__file__).parent.parent
SCRIPTS_DIR = Path(__file__).parent
OUTPUT_DIR = SCRIPTS_DIR / "output"


def run_script(script_name):
    """Run a Python script and return its exit code."""
    script_path = SCRIPTS_DIR / script_name
    print(f"\n{'=' * 60}")
    print(f"Running: {script_name}")
    print(f"{'=' * 60}\n")

    result = subprocess.run(
        [sys.executable, str(script_path)],
        cwd=str(REPO_ROOT),
        capture_output=False,
    )
    return result.returncode


def git_has_changes():
    """Check if there are uncommitted changes in the repo."""
    result = subprocess.run(
        ["git", "status", "--porcelain"],
        cwd=str(REPO_ROOT),
        capture_output=True,
        text=True,
    )
    return bool(result.stdout.strip())


def git_commit_and_push(message):
    """Stage all changes, commit, and push."""
    try:
        subprocess.run(["git", "add", "-A"], cwd=str(REPO_ROOT), check=True)
        subprocess.run(
            ["git", "commit", "-m", message], cwd=str(REPO_ROOT), check=True
        )
        subprocess.run(["git", "push"], cwd=str(REPO_ROOT), check=True)
        print(f"\n✅ Committed and pushed: {message}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Git operation failed: {e}")
        return False


def main():
    timestamp = datetime.now().strftime("%Y-%m-%d")

    print(f"{'#' * 60}")
    print(f"# UKM Event Management — Auto Update")
    print(f"# Date: {timestamp}")
    print(f"{'#' * 60}")

    # Step 1: Check public pages
    public_changes = run_script("scrape-public.py")

    # Step 2: Check for new pekeliling
    pekeliling_changes = run_script("check-pekeliling.py")

    # Step 3: Summary
    print(f"\n{'=' * 60}")
    print(f"SUMMARY")
    print(f"{'=' * 60}")

    total_changes = public_changes + pekeliling_changes

    if total_changes > 0:
        print(f"\n🔔 {total_changes} change(s) detected across all checks.")
        print(f"Review outputs in: {OUTPUT_DIR}/")
        print()

        # Auto-commit the scraper outputs (history, reports)
        if git_has_changes():
            commit_msg = (
                f"auto-update: {timestamp} — "
                f"{total_changes} change(s) detected on UKM pages"
            )
            git_commit_and_push(commit_msg)
        else:
            print("No file changes to commit.")

        print(
            "\n⚠️  ACTION REQUIRED: Review the changes report and manually "
            "update any affected README files if the changes are substantive."
        )
    else:
        print("\n✅ No changes detected. Repo is up to date.")

        # Still commit the updated history timestamps
        if git_has_changes():
            commit_msg = f"auto-update: {timestamp} — no changes detected"
            git_commit_and_push(commit_msg)

    return 0


if __name__ == "__main__":
    exit(main())
