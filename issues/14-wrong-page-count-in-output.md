---
title: "Y2Pal PDF Splitter Wrong Page Count in Output — Fix"
labels: troubleshooting
---

# Y2Pal PDF Splitter Wrong Page Count in Output — Fix

When a split produces output with a different page count than expected — a range of `1-5` yields 4 or 6 pages instead of 5 — the issue is almost always about how absolute PDF page positions differ from the printed page numbers in the source.

## Common Causes & Solutions

### 1. Off-by-One From Printed vs. Absolute Numbering

Scanned books often start page 1 after several pages of front matter (cover, copyright, TOC). Y2Pal uses **absolute PDF page positions** — so "chapter 1 starts at page 1" in the printed book might be PDF page 13.

**Fix**: Open the source in a reader and note the absolute page number (shown at the bottom of viewers like Preview, Adobe Reader). Use that number, not the printed label.

### 2. Range Syntax Misunderstanding

A range of `1-5` includes both endpoints: pages 1, 2, 3, 4, 5 → 5 pages. A range of `1,5` is two single pages: page 1 and page 5 → 2 files of 1 page each.

**Fix**: Use hyphens for continuous ranges, commas to separate distinct ranges.

### 3. Overlapping Ranges Interpreted Correctly

If you type `1-5, 4-8`, Y2Pal produces two files (5 pages each and 5 pages each) — the output is not deduplicated across ranges.

**Fix**: If you want non-overlapping chunks, type non-overlapping ranges. Overlap is intentional and documented.

### 4. Blank / Padding Pages Inflate the Source

A PDF may have blank padding pages (common in print-layout exports, signature-aligned booklets) that inflate the total page count.

**Fix**: Count pages carefully in the source. Blank pages still count as pages.

### 5. Two-Column Layouts Misread as Two Pages

A visual two-column layout is still one PDF page — the physical PDF page count does not change based on visual layout.

**Fix**: No adjustment needed; the count is accurate.

### 6. Mixed Page Sizes

PDFs with mixed page sizes (some A4, some letter, some landscape) sometimes confuse manual counting.

**Fix**: Use the reader's page count (total pages shown in the navigator) as the authoritative number.

### 7. Encrypted PDFs Mask Pages

Rare: some encrypted PDFs have "hidden" pages that only appear after decryption.

**Fix**: Enter the open password and re-check the page count after decryption.

### 8. Update Y2Pal PDF Splitter

Range-parsing logic is updated periodically. The latest server build is always live — reload the page.

## Still Not Working?

- Split a small 10-page PDF with range `1-5` and confirm you get exactly 5 pages.
- If the small test also fails, there is a range-parsing issue — [report it →](https://github.com/AndrewYao93/y2pal-pdf-splitter/issues/new?template=bug_report.md).
- Full [troubleshooting guide](../docs/TROUBLESHOOTING.md).

---

**[Open Y2Pal PDF Splitter →](https://y2pal.com/split-pdf)** | **[Back to README →](https://github.com/AndrewYao93/y2pal-pdf-splitter)**
