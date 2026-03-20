# Contributing & Maintenance Guide

This repo is maintained by the current session's AJK (typically the Bendahari or Setiausaha of the organizing club). This guide explains how to keep it alive and accurate across sessions.

---

## Golden Rules

1. **Never edit PDFs.** These are official UKM documents. If a new version is released, replace the file entirely with the new one (same filename).
2. **Always update `CHANGELOG.md`** when you make changes.
3. **Commit messages** follow this format: `update: [section] — [brief description]`
   - Example: `update: 01-garis-panduan — replaced pekeliling with Bil. 5/2026`
   - Example: `update: 04-perbelanjaan/jamuan — updated rate table for new semester`
4. **Test mermaid flowcharts** — paste them into [mermaid.live](https://mermaid.live/) to verify they render before committing.

---

## Common Maintenance Tasks

### A new Pekeliling Bendahari is released

1. Download the PDF from https://bendahari.ukm.my
2. Replace the relevant file in `01-garis-panduan/` (keep the same filename pattern)
3. Update `01-garis-panduan/README.md` with a summary of what changed
4. Check if the change affects rate tables (`04-perbelanjaan/jamuan/kadar-jamuan.md`)
5. Check if the change affects any flowcharts in `04-perbelanjaan/`
6. Update `CHANGELOG.md`

### A borang is updated

1. Download the new version from Jabatan Bendahari or iSTAR
2. Replace the old file in the correct folder (same filename)
3. Note the new "Tarikh Kuat Kuasa" in the relevant README
4. Update `CHANGELOG.md`

### Adding a new faculty's procedures

1. Create a subfolder under `02-sumber-dana/fakulti/` (e.g., `contoh-fsk/`)
2. Add the faculty's procedure docs
3. Update `02-sumber-dana/fakulti/README.md` to reference the new example
4. Update `CHANGELOG.md`

### Adding a new venue

1. Create a subfolder under `05-tempat-dan-logistik/` (e.g., `dewan-canselor/`)
2. Add a `README.md` with contact info, booking process, and any prerequisites
3. Update `05-tempat-dan-logistik/README.md` to include the new venue
4. Update `CHANGELOG.md`

### Session handover (new AJK takes over)

1. Review all contact info in the repo (UKPEL, venue contacts, faculty HEP)
2. Verify all linked URLs still work
3. Run `python scripts/scrape-public.py` to check for stale content
4. Update any session-specific references (e.g., "Sesi 2025/2026" → "Sesi 2026/2027")
5. Update `CHANGELOG.md` with a handover entry

---

## File Naming Conventions

| Type | Convention | Example |
|------|-----------|---------|
| Folders | `kebab-case` in BM | `04-perbelanjaan` |
| Official PDFs | `kebab-case`, descriptive | `borang-pesanan-jamuan.pdf` |
| Markdown guides | `README.md` or descriptive | `kadar-jamuan.md` |
| Org-specific examples | Inside `contoh-[org]/` subfolder | `contoh-pertama/borang-pendahuluan-pertama.pdf` |

---

## Automation

The repo includes scripts in `scripts/` and a GitHub Actions workflow in `.github/workflows/monthly-check.yml` that automatically check public UKM pages for updates.

### Running scripts manually

```bash
# Install dependencies
pip install -r scripts/requirements.txt

# Check public pages for changes
python scripts/scrape-public.py

# Check for new pekeliling
python scripts/check-pekeliling.py

# Full auto-update (scrape → diff → commit)
python scripts/auto-update.py
```

### Credential management

For login-walled pages (SMPR, iSTAR), the scripts use a `.env` file:

```bash
# Copy the template
cp .env.example .env

# Fill in your credentials
nano .env
```

**⚠️ NEVER commit `.env` to the repo.** It's in `.gitignore` but double-check before pushing.

For GitHub Actions, add credentials as **repository secrets** (Settings → Secrets and Variables → Actions).

---

## Questions?

If you're stuck, check `panduan-pantas/glosari.md` for term definitions or open an issue on the repo.
