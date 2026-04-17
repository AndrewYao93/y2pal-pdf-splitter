---
title: "How to Split a PDF Every N Pages — Equal-Size Chunks"
labels: guide
---

# How to Split a PDF Every N Pages

"Every N pages" mode divides a PDF into fixed-size chunks: 10 pages per file, 25 pages per file, 50 pages per file. It's the tool for statements that repeat on a known cadence, for print-layout exports where each N-page unit is a signature, and for email-sized chunking.

## When to Use Every-N Mode

| Scenario                                  | Suggested N |
|-------------------------------------------|-------------|
| Monthly statement with 1 page per day     | 31          |
| Weekly report bundle with 5 pages each    | 5           |
| Print signature (multi-up booklet)        | 8 or 16     |
| Email-sized chunks (25 MB / ~0.5 MB/page) | 50          |
| Study guide, one unit per 10-page section | 10          |

## Step-by-Step Guide

### Step 1: Upload the Source PDF

Visit [y2pal.com/split-pdf](https://y2pal.com/split-pdf). Drag or pick the source file.

### Step 2: Select Every-N-Pages Mode

Choose **Split every N pages**. A single numeric input appears.

### Step 3: Enter N

Type the chunk size. A 100-page source with `N = 25` yields 4 output files of 25 pages each. A 103-page source with `N = 25` yields 4 files: three of 25 pages plus a final file of 3 pages (the remainder).

### Step 4: Confirm Count

The UI shows the resulting file count before you commit. If the count seems off, re-check `N` and the source page total.

### Step 5: Split and Download

Click **Split PDF**. Output files are named sequentially: `source_part_01.pdf`, `source_part_02.pdf`, etc.

## Edge Cases

| Scenario                    | Behavior                               |
|-----------------------------|----------------------------------------|
| Source has fewer pages than N | One output file = the whole source   |
| Source has an odd remainder | Final file contains the remainder      |
| `N = 1`                     | Each page becomes its own file         |
| `N = 0` or negative         | Rejected with validation error         |

## Comparing to Page-Range Mode

Every-N gives uniform chunks; page-range gives custom chunks. Use:

- **Every-N** when chunks should be identical in size (statements, print signatures, email pieces).
- **Page-range** when chunks correspond to meaningful semantic boundaries (chapters, exhibits, sections).

## Tips

1. For statements with one page per entity (e.g. one page per customer invoice), `N = 1` extracts every page as its own file.
2. Combine with bookmark detection in a two-step flow: first split at bookmarks to get per-section PDFs, then use every-N within a section if needed.
3. If the output count seems wrong, double-check that the source PDF doesn't have blank padding pages at the end that inflate the count.

## Requirements

- A source PDF with at least `N` pages (or fewer, which produces a single output).
- Any modern browser.
- A device with enough disk space for the combined output size.

---

**[Open Y2Pal PDF Splitter →](https://y2pal.com/split-pdf)** | **[Back to README →](https://github.com/AndrewYao93/y2pal-pdf-splitter)**
