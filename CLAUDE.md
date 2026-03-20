# CLAUDE.md — Repository Context for Claude Code

## About This Repository

This is a consolidated guide for managing student programs and finances at Universiti Kebangsaan Malaysia (UKM). It organizes official UKM documents (pekeliling, borang, garis panduan) alongside plain-language markdown guides to make UKM's bureaucratic procedures accessible.

## Language

All READMEs and guides are written in **English**, with **BM terms preserved** for official names:
- Document names: Pekeliling Bendahari, Borang Pesanan Jamuan, Kertas Kerja, Laporan Kewangan
- System names: eP@UKM, iFASt, iSTAR, SMPR, UKPEL
- Procedure names: Pesanan Rasmi, pendahuluan, Borang Pink, Caj Antara Jabatan
- Position titles: Bendahari, Penasihat, Dekan
- Folder names remain in BM kebab-case

## Folder Structure

```
01-garis-panduan/        → Official UKM policies & circulars
02-sumber-dana/          → Funding sources (HEP, Faculty, KMUKM, Sponsorship)
03-belanjawan/           → Budget templates & examples
04-perbelanjaan/         → Spending procedures (pendahuluan, Pesanan Rasmi, jamuan, etc.)
05-tempat-dan-logistik/  → Venue booking & equipment
06-laporan-kewangan/     → Post-event financial reporting
07-latihan/              → Training modules & slides
panduan-pantas/          → Checklists, timelines, glossary
scripts/                 → Automation scripts (Python)
```

## File Naming Conventions

- Folders: `kebab-case` in BM (e.g., `01-garis-panduan`)
- Official UKM PDFs: descriptive `kebab-case` (e.g., `borang-pesanan-jamuan.pdf`)
- Markdown guides: `README.md` in each folder, or descriptive names (e.g., `kadar-jamuan.md`)
- Org-specific examples: placed in `contoh-pertama/` or `contoh-[org-name]/` subfolders

## Editing Rules

1. **NEVER edit PDFs** — these are official UKM documents. Only replace with newer official versions.
2. **README.md** files are the authored content — these can and should be updated.
3. Every procedure MUST have a mermaid flowchart showing the A-to-Z flow.
4. Every flowchart step involving a form MUST tag the borang name/code.
5. Update `CHANGELOG.md` with every change.
6. Commit messages follow: `update: [section] — [brief description]`

## Critical UKM Thresholds

These numbers drive most decision trees in the repo:

| Threshold | What It Means |
|-----------|---------------|
| **RM500** | Below = Borang Pink / Pendahuluan / Tuntutan Bayaran Balik. At or above = Pesanan Rasmi via eP@UKM |
| **RM3,000** | Above this = Pesanan Rasmi handled by Bahagian Perolehan, Jabatan Bendahari (not HEP-UKM) |
| **2 weeks before event** | Minimum lead time for Pesanan Rasmi submission and Pendahuluan submission to UKPEL |
| **1–3 working days** | eP@UKM broadcast/advertisement period for registered suppliers to bid |
| **30 days after event** | Deadline for Laporan Kewangan (Pendahuluan type) |
| **60 days after event** | Deadline for Laporan Kewangan (Tuntutan type) |
| **14 working days** | Jabatan Bendahari payment processing time |
| **6 hours / 12:30pm** | Program duration thresholds for jamuan eligibility (Pindaan Bil. 4/2025) |

## Key UKM URLs

| System | URL | Notes |
|--------|-----|-------|
| Jabatan Bendahari | https://bendahari.ukm.my | Main finance office portal |
| Portal Pelajar Bendahari | https://bendahari.ukm.my/student_portal | Submit pendahuluan & laporan kewangan online |
| eP@UKM (e-Perolehan) | https://ukmperolehan.ukm.my/ | Procurement system for Pesanan Rasmi |
| SMPR | https://ewarga.ukm.my/smpr/index.cfm | Room/venue booking system (requires login) |
| IVI Facilities | https://ivi.ukm.my/facilities/ | AST venue info |
| UKM Trademark | https://www.ukm.my/inovasi-ukm/ | List of licensed UKM logo vendors |

## Update Workflow

When updating this repo:
1. Run `python scripts/scrape-public.py` to check public UKM pages
2. Review output in `scripts/output/` for changes
3. Update the relevant README.md files
4. Update `CHANGELOG.md`
5. Commit with format: `update: [section] — [brief description]`
