---
title: "How to Extract Specific Pages from a PDF — Single-Page Isolation"
labels: guide
---

# How to Extract Specific Pages from a PDF

Extracting specific pages — a signed signature page, a certificate of insurance, the conclusions section of a report — is technically a specialized case of splitting. Y2Pal PDF Splitter handles single-page and multi-page extraction with the same page-range interface.

## Common Extract-Only Use Cases

- Pull a single signature page from a 200-page contract bundle.
- Isolate a certificate of insurance from a multi-document proof packet.
- Extract only the executive summary from a long report.
- Grab pages 3, 7, and 42 without the pages between them.
- Lift an appendix table without its surrounding content.

## Step-by-Step Guide

### Step 1: Identify Target Pages

Note the exact pages you want. Extracting page 42 alone is different from extracting pages 42–44.

### Step 2: Upload

Visit [y2pal.com/split-pdf](https://y2pal.com/split-pdf) and upload the source PDF.

### Step 3: Use Page-Range Syntax

Select **Split by page range**. For a single page, type just the page number:

```
42
```

For multiple non-contiguous pages, use commas:

```
3, 7, 42
```

Each number becomes its own output file (3 files in the above example). To combine them into one output, use a continuous range:

```
3-7
```

### Step 4: Handle Special Cases

- **Last page only** — if the PDF has 200 pages and you need the last, type `200`.
- **All pages except a few** — type the kept ranges (e.g. `1-41, 43-200` to drop page 42).

### Step 5: Download Individually or as Zip

For 1–3 pages, individual downloads are easier. For 10+ pages, use **Download All** → zip.

## Single-Page vs Range Output

| Input       | Output                          |
|-------------|---------------------------------|
| `7`         | One file with page 7 only       |
| `7, 7`      | Two identical single-page files |
| `7-7`       | One file with page 7 only       |
| `7, 9, 11`  | Three single-page files         |
| `7-11`      | One file with pages 7-11        |

## Tips

1. To **swap pages** (keep page 42 but drop pages 40–41), extract the ranges separately (`1-39, 42, 43-200`) and the resulting files are gap-free.
2. Absolute page positions are what matters — if page 7 is labeled "Page iii" in the source, Y2Pal still treats it as position 7.
3. For workflows that combine extraction and re-merging, use Y2Pal's companion tool, PDF Merger, after extracting.

## Requirements

- The source PDF.
- Exact page numbers (1-based, absolute positions).
- Any modern browser.

---

**[Open Y2Pal PDF Splitter →](https://y2pal.com/split-pdf)** | **[Back to README →](https://github.com/AndrewYao93/y2pal-pdf-splitter)**
