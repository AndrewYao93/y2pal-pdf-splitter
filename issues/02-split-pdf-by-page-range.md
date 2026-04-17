---
title: "How to Split a PDF by Page Range — Exact Page Numbers"
labels: guide
---

# How to Split a PDF by Page Range

Splitting a PDF at exact page boundaries is the most common workflow: isolate chapter 3, extract pages 40–55, or pull the appendix out of a 300-page report. Y2Pal PDF Splitter's page-range mode handles comma-separated ranges in one pass.

## Why Split by Page Range?

- Page-range splitting gives **per-chunk control** that bookmark or every-N modes cannot match.
- Multiple ranges produce multiple output files in a single operation.
- Works on any PDF, including scanned PDFs without structural bookmarks.
- No need to memorize chapter titles — page numbers are enough.

## Step-by-Step Guide

### Step 1: Identify the Target Pages

Open the source PDF in any reader and note the page numbers you want to keep. Example:

- Introduction: pages 1–5
- Methodology: pages 8–15
- Appendix: pages 40–52

### Step 2: Upload to Y2Pal

Visit [y2pal.com/split-pdf](https://y2pal.com/split-pdf), drag the PDF onto the drop zone.

### Step 3: Enter the Ranges

Select **Split by page range** and type:

```
1-5, 8-15, 40-52
```

Each range becomes one output file. Use commas to separate ranges, hyphens for continuous ranges, and single numbers for single pages.

### Step 4: Preview and Confirm

The tool shows a live count of how many output PDFs will be produced (3 in this example). Click **Split PDF**.

### Step 5: Download

Each output file appears with its range in the filename, e.g. `source_pages_1-5.pdf`.

## Range Syntax Reference

| Input              | Meaning                                |
|--------------------|----------------------------------------|
| `1-5`              | Pages 1 through 5 inclusive → 1 file   |
| `1-5, 10-15`       | Two separate ranges → 2 files          |
| `7`                | Single page 7 → 1 file                 |
| `1, 3, 5`          | Three individual pages → 3 files       |
| `1-5, 4-8`         | Overlapping ranges allowed → 2 files   |
| `100-50`           | Invalid (start > end) → error shown    |

## Tips

1. Use single page numbers (e.g. `7`) to extract one page as a standalone PDF without any bundle.
2. The tool uses 1-based absolute page positions — page 1 is the first page of the PDF file, not the printed "page 1" of a scanned book.
3. For very long range lists, paste from a spreadsheet — the input accepts multi-line paste.

## Requirements

- Source PDF in a supported version (PDF 1.4 – 2.0).
- For encrypted PDFs, the open password must be supplied.
- Browser with JavaScript enabled.

---

**[Open Y2Pal PDF Splitter →](https://y2pal.com/split-pdf)** | **[Back to README →](https://github.com/AndrewYao93/y2pal-pdf-splitter)**
