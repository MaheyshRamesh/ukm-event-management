# Repository Plan — `ukm-event-management`

> This document is the source of truth for the repo's scope, structure, conventions, and implementation roadmap. It was finalized before any content was written and should be updated if the plan changes.

---

## 1. Purpose

A single GitHub repository that any UKM student organization can use to understand and execute the **full lifecycle of running a program** — from idea to final financial report submission. No more hunting through random Google Drives or asking seniors "eh mana borang tu?"

## 2. Target Audience

**Primary:** Bendahari, Setiausaha, Ketua Program, and AJK of any kelab/persatuan/kolej kediaman under UKM.  
**Secondary:** Faculty HEP staff looking for a consolidated reference.

## 3. Key Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| **README language** | English, with BM terms preserved for official names (e.g., Pesanan Rasmi, Borang Pink, pendahuluan, UKPEL) | Accessible to wider audience while keeping UKM-specific terminology accurate |
| **Repo scope** | Generic UKM (any student org) | FTSM/PERTAMA-specific files included as labeled examples, not as THE guide |
| **Penajaan Excel files** | Included as reference templates | `senarai-penajaan-1.xlsx` and `senarai-penajaan-2.xlsx` |
| **Automation approach** | Full autonomous (auto-commit via GitHub Actions) | Maintainer accepts the risk; `.env` + `.gitignore` for credentials |
| **Claude Code support** | Yes — `CLAUDE.md` included at root | Enables Claude Code to understand repo context and make updates |
| **Flowcharts** | Mermaid diagrams in every procedure README, A-to-Z with borang names tagged | Renders natively on GitHub |

## 4. Folder Structure

```
ukm-event-management/
│
├── README.md                          # Repo overview, lifecycle flowchart, quickstart
├── PLAN.md                            # THIS FILE — the repo blueprint
├── CLAUDE.md                          # Claude Code context file
├── CONTRIBUTING.md                    # How future maintainers update the repo
├── CHANGELOG.md                       # Track all updates
├── LICENSE                            # CC BY-SA 4.0
├── .gitignore                         # Ensures .env never gets committed
├── .env.example                       # Template for scraper credentials
│
├── 01-garis-panduan/                  # Official UKM policies & circulars
│   ├── README.md                      # Summary of each policy, key thresholds
│   ├── pindaan-bil-4-2025.pdf
│   ├── garis-panduan-kewangan-kegiatan-pelajar.pdf
│   └── infografik-kewangan-ukm.pdf
│
├── 02-sumber-dana/                    # Where the money comes from
│   ├── README.md                      # Decision tree: which source for what
│   ├── hep-ukm/
│   │   └── README.md                  # PLACEHOLDER — maintainer to add HEP-specific docs later
│   ├── fakulti/
│   │   ├── README.md                  # Generic faculty process + FTSM as worked example
│   │   ├── prosedur-permohonan-dana-ftsm.pdf
│   │   └── borang-permohonan-dana.pdf
│   ├── kmukm/
│   │   ├── README.md                  # KMUKM dana application A-to-Z, pitching process
│   │   ├── buku-panduan-dana-kmukm.pdf
│   │   └── borang-aku-janji.pdf
│   └── penajaan/
│       ├── README.md                  # Sponsorship workflow, tax exemption, Borang Derma
│       ├── kit-penajaan-contoh-1.pdf
│       ├── kit-penajaan-piala-dekan.pdf
│       ├── prospektus-tewo-contoh.pdf
│       ├── surat-penajaan-template.docx
│       ├── surat-pengecualian-cukai.pdf
│       ├── borang-permohonan-derma.pdf
│       ├── senarai-penajaan-1.xlsx
│       └── senarai-penajaan-2.xlsx
│
├── 03-belanjawan/                     # Budgeting
│   ├── README.md                      # How to build a compliant budget, common mistakes
│   ├── contoh-templat-belanjawan.pdf
│   └── contoh-belanjawan-bengkel.pdf
│
├── 04-perbelanjaan/                   # Spending & procurement (THE most critical section)
│   ├── README.md                      # MASTER GUIDE: decision tree for all spending methods
│   ├── pendahuluan/
│   │   ├── README.md                  # Cash advance process A-to-Z
│   │   ├── borang-pendahuluan-ukm.pdf
│   │   └── contoh-pertama/
│   │       └── borang-pendahuluan-pertama.pdf
│   ├── pesanan-rasmi/
│   │   └── README.md                  # eP@UKM flow, 2-week lead time, HEP broadcast step
│   ├── jamuan/
│   │   ├── README.md                  # Borang Pink (<RM500) vs Pesanan Rasmi (≥RM500)
│   │   ├── borang-pesanan-jamuan.pdf
│   │   └── kadar-jamuan.md            # Rate table from Pekeliling Bil.8/2022 + Bil.4/2025
│   ├── bayaran-terus/
│   │   └── README.md                  # Direct payment: panel, penceramah, yuran penyertaan
│   ├── caj-antara-jabatan/
│   │   └── README.md                  # iFASt — internal UKM services
│   └── contoh-pertama/
│       └── borang-pinjaman-kewangan.pdf
│
├── 05-tempat-dan-logistik/            # Venue booking & equipment
│   ├── README.md                      # Overview of all venue booking pathways at UKM
│   ├── ast/
│   │   └── README.md                  # AST: IVI link, contact Salleh, SMPR, iStar prerequisite
│   ├── kolej-kediaman/
│   │   └── README.md                  # PLACEHOLDER for KPZ and other kolej
│   └── borang-peralatan-kemudahan-majlis.pdf
│
├── 06-laporan-kewangan/               # Post-event financial reporting
│   ├── README.md                      # What to submit, deadlines, common rejection reasons
│   ├── format-surat-serahan.pdf
│   ├── pengakuan-penyerahan.pdf
│   ├── contoh-laporan-ffh.pdf
│   └── contoh-laporan-kongsi-rezeki.pdf
│
├── 07-latihan/                        # Training materials
│   ├── README.md
│   ├── modul-kewangan-pertama-2526.pdf
│   └── slide-deck-semasa.pdf
│
├── panduan-pantas/                    # Quick references
│   ├── senarai-semak-bendahari.md     # Pre/during/post event checklist
│   ├── garis-masa-program.md          # T-minus countdown (8 weeks → event day → +30 days)
│   └── glosari.md                     # UKPEL, eP@UKM, iFASt, iStar, SMPR, Borang Pink, etc.
│
├── scripts/                           # Automation
│   ├── scrape-public.py               # Scrape public UKM pages for updates
│   ├── check-pekeliling.py            # Check for new Bendahari circulars
│   ├── auto-update.py                 # Orchestrator: fetch → diff → commit
│   ├── requirements.txt
│   └── output/                        # Scraper output directory (gitignored)
│
└── .github/
    └── workflows/
        └── monthly-check.yml          # GitHub Actions — scheduled scrape + auto-commit
```

## 5. Content Rules

### What Gets Written (13 markdown files)

1. **Root `README.md`** — lifecycle flowchart, repo navigation, quick decision tree
2. **`CLAUDE.md`** — Claude Code context (thresholds, naming conventions, edit rules)
3. **`CONTRIBUTING.md`** — how to add borang, update pekeliling, naming conventions
4. **`CHANGELOG.md`** — version history
5. **7 section `README.md` files** — one per numbered folder, each with:
   - Plain-language explanation of the procedure
   - Mermaid flowchart showing A-to-Z steps
   - Borang names/codes tagged at each relevant step
   - List of files in that folder with descriptions
6. **3 cheatsheets** in `panduan-pantas/`:
   - `senarai-semak-bendahari.md` — checkbox-style checklist
   - `garis-masa-program.md` — reverse timeline from T-8 weeks
   - `glosari.md` — glossary of UKM-specific acronyms and terms

### Sub-section READMEs (8 more markdown files)

- `02-sumber-dana/hep-ukm/README.md` — placeholder
- `02-sumber-dana/fakulti/README.md` — generic + FTSM example
- `02-sumber-dana/kmukm/README.md` — full KMUKM guide
- `02-sumber-dana/penajaan/README.md` — sponsorship workflow
- `04-perbelanjaan/pendahuluan/README.md` — cash advance guide
- `04-perbelanjaan/pesanan-rasmi/README.md` — eP@UKM procurement guide
- `04-perbelanjaan/jamuan/README.md` — food & beverage guide
- `05-tempat-dan-logistik/ast/README.md` — AST venue guide

Plus: `04-perbelanjaan/jamuan/kadar-jamuan.md` (rate table), `04-perbelanjaan/bayaran-terus/README.md`, `04-perbelanjaan/caj-antara-jabatan/README.md`, `05-tempat-dan-logistik/kolej-kediaman/README.md`

### Language Convention

- **English** for all explanations, headers, descriptions
- **BM preserved** for: official document names, borang names, UKM system names (eP@UKM, iFASt, iSTAR, SMPR, UKPEL), procedure names (Pesanan Rasmi, pendahuluan, Borang Pink), position titles (Bendahari, Penasihat), and folder names
- **No Manglish** — keep it clean and professional

### Flowchart Rules

- Every procedure section MUST have a mermaid flowchart
- Every step involving a form/borang MUST tag the borang name
- Decision nodes must clearly show the threshold (e.g., "< RM500" vs "≥ RM500")
- Flowcharts should be readable top-to-bottom or left-to-right
- Include timing requirements at relevant steps (e.g., "⚠️ 2 minggu sebelum program")

## 6. Deduplication

Source files that were duplicates and were excluded:

| Kept | Dropped |
|------|---------|
| `26102023BUKU_PANDUAN_LENGKAP_DANA_KMUKM.pdf` | Both `.docx` versions (same content) |
| `Infografik_...UKM.pdf` | The `_copy` version (identical) |
| `Format_Surat_Serahan_..._copy.pdf` | The `_pdf_20250519` version |

Final count: **28 unique source files** in repo.

## 7. Automation Design

### Full Autonomous Flow

```
GitHub Actions (monthly cron)
    → scripts/auto-update.py
        → scrape-public.py (fetch public UKM pages)
        → check-pekeliling.py (check for new circulars)
        → diff against current repo content
        → if changes detected:
            → update relevant README sections
            → update CHANGELOG.md
            → git commit + push directly to main
```

### Credential Handling

- `.env` file at repo root (gitignored) stores login credentials for ewarga/iStar
- `.env.example` shows required variables without real values
- GitHub Actions uses repository secrets for scheduled runs
- Login-walled scraping (SMPR, iStar) included in auto-update but will gracefully fail if credentials are invalid/expired — maintainer re-authenticates manually when needed

### Public Pages Scraped

| URL | What We Check |
|-----|---------------|
| `https://bendahari.ukm.my` | New pekeliling, updated borang |
| `https://ivi.ukm.my/facilities/` | AST facility changes, contact info |
| `https://ukmperolehan.ukm.my/` | eP@UKM system changes |

### Login-Walled Pages (requires credentials)

| URL | What We Check |
|-----|---------------|
| `https://ewarga.ukm.my/smpr/index.cfm` | SMPR system changes |

## 8. Implementation Order

| # | Task | Priority |
|---|------|----------|
| 1 | ✅ Create folder structure + copy all source files | Done |
| 2 | ✅ Write `PLAN.md` (this file) | Done |
| 3 | Write `CLAUDE.md` | High |
| 4 | Write root `README.md` with lifecycle flowchart | High |
| 5 | Write `04-perbelanjaan/` READMEs (highest-value section) | High |
| 6 | Write `05-tempat-dan-logistik/` READMEs (new undocumented info) | High |
| 7 | Write `02-sumber-dana/` READMEs | Medium |
| 8 | Write `01-garis-panduan/README.md` | Medium |
| 9 | Write `03-belanjawan/README.md` | Medium |
| 10 | Write `06-laporan-kewangan/README.md` | Medium |
| 11 | Write `07-latihan/README.md` | Low |
| 12 | Write `panduan-pantas/` cheatsheets | Medium |
| 13 | Write `CONTRIBUTING.md` | Medium |
| 14 | Write `CHANGELOG.md` | Low |
| 15 | Write automation scripts + GitHub Actions workflow | Low |
| 16 | Write `.gitignore`, `.env.example`, `LICENSE` | Low |
| 17 | Final review pass | — |

## 9. Critical UKM Thresholds (Reference)

These numbers drive most of the decision trees in this repo:

| Threshold | Significance |
|-----------|-------------|
| **RM500** | Below = Borang Pink / Pendahuluan / Tuntutan. At or above = Pesanan Rasmi (eP@UKM) |
| **RM3,000** | Above = Pesanan Rasmi handled by Bahagian Perolehan, Jabatan Bendahari (not HEP) |
| **2 weeks before event** | Minimum lead time for Pesanan Rasmi and Pendahuluan submission |
| **1–3 working days** | eP@UKM broadcast/advertisement period for supplier bidding |
| **30 days after event** | Deadline for Laporan Kewangan (Pendahuluan) |
| **60 days after event** | Deadline for Laporan Kewangan (Tuntutan) |
| **14 working days** | Payment processing time by Jabatan Bendahari |
| **6 hours / 12:30pm** | Program duration thresholds for jamuan eligibility (Pindaan Bil. 4/2025) |

---

*Last updated: March 2026*
