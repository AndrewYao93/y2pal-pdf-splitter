---
title: "How to Split a Large PDF File (Over 100 MB) Online"
labels: guide
---

# How to Split a Large PDF File

Large PDFs — scanned books, legal filings, merged annual reports — routinely exceed 100 MB and occasionally cross 500 MB. They're painful to email, slow to open, and often rejected by upload forms. Splitting them into smaller pieces is the standard remedy.

## Why Large PDFs Are Painful

- Email attachment caps are typically 25 MB (Gmail) or 35 MB (Outlook).
- Cloud-storage sync stalls on files over 1 GB.
- Legal e-filing portals often reject PDFs over 50 MB.
- Mobile PDF readers struggle with files over 100 MB.

Splitting the file sidesteps all four problems.

## Step-by-Step Guide

### Step 1: Check the Free-Tier Cap

The free-tier upload cap is shown at the top of [y2pal.com/split-pdf](https://y2pal.com/split-pdf). If your file exceeds it, two options:

- Upgrade to a lifetime license for higher caps.
- Split the file locally first with a desktop tool to halve the size, then upload each half to Y2Pal for finer splitting.

### Step 2: Upload on a Stable Connection

Large uploads need bandwidth. Wired ethernet or home Wi-Fi is preferred over hotel/airport captive portals, which sometimes silently cap POST payload size.

### Step 3: Pick a Chunking Mode

For a large PDF, **every N pages** is often the right call:

- If the target is "email-sized pieces", estimate ~1 MB per page for scanned PDFs and set `N` so `N × 1 MB ≤ 25 MB`.
- For born-digital text PDFs, 1 page ≈ 100 KB, so `N = 200` gives ~20 MB chunks.

### Step 4: Download as ZIP

For 10+ output pieces, use **Download All** — the browser's per-file download limit makes individual downloads tedious past a handful.

## File-Size Reference (Rough Estimates)

| Source Type            | Avg. MB / page | Split Strategy                |
|------------------------|----------------|-------------------------------|
| Text-only PDF (born-digital) | 0.05–0.15 MB | Every N=200 for ~20 MB chunks|
| Mixed text + images    | 0.3–0.8 MB     | Every N=50                    |
| Scanned book (600 DPI) | 0.8–2.5 MB     | Every N=20                    |
| Photo-heavy brochure   | 1.5–5 MB       | Every N=10                    |

## Tips

1. If upload stalls near 99%, check the page header for size-cap messaging before retrying — the server may reject the POST after transfer.
2. For PDFs over 500 MB, use a desktop tool for the first split, then Y2Pal for finer work — large single uploads are bandwidth-bound.
3. The **Download All** zip is generated on-demand; if the browser times out, retry the zip generation once.

## Requirements

- Sufficient upload bandwidth (10 Mbps+ recommended for 100 MB+ files).
- 1 GB+ free local disk for downloads.
- A browser tab that can stay open during upload (large uploads can take several minutes).

---

**[Open Y2Pal PDF Splitter →](https://y2pal.com/split-pdf)** | **[Back to README →](https://github.com/AndrewYao93/y2pal-pdf-splitter)**
