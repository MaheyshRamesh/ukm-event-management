# Jamuan (Food & Beverages)

Jamuan is one of the most regulated expenses in UKM programs. The rules depend on **where** the program is held and **how much** the total jamuan costs.

---

## Decision Tree: Which Jamuan Route?

```mermaid
flowchart TD
    A["Need jamuan\nfor your program?"] --> B{"Program held\nin-campus or\noff-campus?"}
    B -->|"In-Campus\n(UKM & sekitar UKM)"| C{"Total jamuan\namount?"}
    B -->|"Off-Campus"| OC["Can use Pendahuluan\nfor food expenses.\nMust provide: participant count,\nmenu, and per-pax rate."]
    
    C -->|"< RM500"| BP["Route A:\nBorang Pesanan Jamuan\n(Borang Pink)"]
    C -->|"≥ RM500"| PR["Route B:\nPesanan Rasmi\n(eP@UKM)"]
    
    BP --> BP1["1. Get Borang Pink from\nPejabat HEP-UKM"]
    BP1 --> BP2["2. Get Pusat Tanggungjawab\nsignature (Penasihat)"]
    BP2 --> BP3["3. Submit to Kewangan\nHEP-UKM with:\n• Kertas Kerja iSTAR\n• Surat Kelulusan iSTAR\n• Surat Kelulusan Dana\n• Senarai nama peserta"]
    BP3 --> BP4["4. Agree on menu & price\nwith vendor\n(no formal quotation needed)"]
    
    PR --> PR1["Follow full\nPesanan Rasmi procedure\n(see pesanan-rasmi/)\nAdditional docs:\n• Sebut harga from vendor\n• Senarai nama peserta"]
```

## Jamuan Eligibility Rules (Post Pindaan Bil. 4/2025)

| Program Duration | Crossing 12:30pm? | What You Can Provide |
|------------------|--------------------|----------------------|
| > 6 hours | — | Jamuan Ringan + Makan Tengah Hari |
| < 6 hours | Yes, crosses 12:30pm | Jamuan Ringan **or** Makan Tengah Hari |
| < 6 hours | No | Jamuan Ringan only |
| Any duration | Involves LPU Chair / VC / external guests | Jamuan Ringan + Makan Tengah Hari |

## In-Campus Vendor Requirement

For programs **within UKM and surrounding area**, you MUST use food vendors registered with UKM (pembekal berdaftar). You cannot simply buy from external restaurants and claim receipts.

## Rate Ceilings

Jamuan rates must comply with Pekeliling Bendahari Bil. 8/2022. The specific per-pax rates are set in the pekeliling — refer to [`01-garis-panduan/pindaan-bil-4-2025.pdf`](../../01-garis-panduan/pindaan-bil-4-2025.pdf) for the latest rates.

> **Tip:** When preparing your belanjawan, always check the current pekeliling rates first. Budget items exceeding the rate ceiling will be **rejected by Kewangan HEP-UKM** even if your overall budget is approved.

## Files in This Folder

| File | Description |
|------|-------------|
| `borang-pesanan-jamuan.pdf` | Borang Permohonan Pesanan Jamuan (UKM-SPKPPP-PP04-BO02) — effective 06 Jun 2025 |
