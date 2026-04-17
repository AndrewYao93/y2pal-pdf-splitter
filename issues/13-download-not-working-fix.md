---
title: "Y2Pal PDF Splitter Download Not Working — Fix Guide"
labels: troubleshooting
---

# Y2Pal PDF Splitter Download Not Working — Fix Guide

Processing succeeds but the download button doesn't trigger, the zip is empty, or the file saves with a generic name. Here are the common causes and fixes.

## Common Causes & Solutions

### 1. Browser Blocks Pop-Up Downloads

Chrome, Firefox, and Edge block unexpected programmatic downloads if pop-up blocking is strict.

**Fix**: Click the address-bar icon that appears during a blocked download and choose "Always allow downloads from y2pal.com".

### 2. "Unsafe Download" Warning

Chrome marks PDF downloads as "may be dangerous" by default. Not a bug — a Chromium safety feature.

**Fix**: Click **Keep** in the download shelf. On corporate machines, ask IT to allowlist downloads from `y2pal.com`.

### 3. ZIP Generation Times Out

When splitting into 50+ output files, the zip-bundling step can time out if the server is under load.

**Fix**: Retry the **Download All** action — transient timeouts usually recover. As a fallback, download output files individually.

### 4. Safari Auto-Expands ZIP

iOS and macOS Safari auto-expands downloaded zips by default and then deletes the zip.

**Fix**: Change Safari preferences (macOS): Safari → Settings → General → uncheck "Open 'safe' files after downloading." On iOS, use the Files app's long-press to save the zip without extracting.

### 5. Generic Filename (download.pdf)

Some mobile browsers strip the `Content-Disposition` header, causing descriptive filenames to be lost.

**Fix**: Rename manually after download. Or use the desktop browser for workflow-critical naming.

### 6. Session Expired During Processing

If processing takes longer than the session timeout (rare, ~30 min), the download links may return a 404.

**Fix**: Re-run the split from scratch. Long processing times usually indicate a very large source file — consider local pre-splitting.

### 7. Download Blocked by Corporate Policy

Some DLP (data-loss prevention) suites block downloads from non-allowlisted services.

**Fix**: Request an exception for `y2pal.com` from IT, or work from a personal device.

### 8. Disk Full

A PDF download refuses to save if local disk has less free space than the file size.

**Fix**: Free up disk space, then retry.

## Still Not Working?

- Test with a small 5-page PDF to confirm whether the issue is download-specific or processing-specific.
- Check browser console for specific error codes — report those in a bug issue.
- [Open a bug report →](https://github.com/AndrewYao93/y2pal-pdf-splitter/issues/new?template=bug_report.md)

---

**[Open Y2Pal PDF Splitter →](https://y2pal.com/split-pdf)** | **[Back to README →](https://github.com/AndrewYao93/y2pal-pdf-splitter)**
