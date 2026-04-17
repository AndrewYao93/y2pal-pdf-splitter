---
title: "Y2Pal PDF Splitter Upload Failed — How to Fix"
labels: troubleshooting
---

# Y2Pal PDF Splitter Upload Failed — How to Fix

When a PDF upload to Y2Pal PDF Splitter fails, the cause is almost always network-, size-, or file-format-related. Work through the following common causes.

## Common Causes & Solutions

### 1. File Exceeds Free-Tier Cap

The free tier has a maximum file size shown at the page header. If your PDF is above the cap, the server rejects the POST after it completes — producing a late "upload failed" error.

**Fix**: Check the page header first. If over the cap, upgrade to a lifetime license for larger caps, or pre-split locally.

### 2. Unstable Network

Upload stalls and times out on hotel Wi-Fi, captive portals, or mobile hotspot with weak signal.

**Fix**: Switch to a wired/home network. Test with a small file first to confirm bandwidth.

### 3. File Not a Valid PDF

Files saved with `.pdf` extension but containing corrupted or truncated data are rejected at parse.

**Fix**: Open the file locally first. If your native PDF reader can't open it, re-export from the source application.

### 4. Browser Extension Interference

Ad blockers and privacy extensions sometimes break multipart form uploads.

**Fix**: Disable extensions for `y2pal.com` or try an incognito/private window.

### 5. Corporate Proxy / Firewall

Deep-packet inspection proxies (Zscaler, Netskope, Cisco Umbrella) occasionally strip multipart boundaries.

**Fix**: Request an allowlist for `*.y2pal.com` from IT, or use a personal hotspot as a diagnostic.

### 6. iOS / Android Tab Suspension

Mobile browsers suspend background tabs aggressively, interrupting long uploads.

**Fix**: Keep the Y2Pal tab in the foreground during upload. Disable Low Power Mode on iOS. For large files, prefer desktop browsers.

### 7. Drag-Drop Not Working

Drag events from some file managers (Linux Wayland + Firefox, macOS Finder to Safari occasionally) don't forward MIME data.

**Fix**: Click **Upload File** instead to open the native file picker.

### 8. HTTPS Certificate Warnings

A corporate man-in-the-middle cert may trigger a CORS or cert error on upload.

**Fix**: Work from a personal device, or request that IT excludes `y2pal.com` from TLS inspection.

## Still Not Working?

- Try a 1-page test PDF first to isolate whether the issue is file-specific or network-specific.
- Clear browser site data for `y2pal.com` and reload.
- Check the full [troubleshooting guide](../docs/TROUBLESHOOTING.md) for edge cases.
- [Open a bug report →](https://github.com/AndrewYao93/y2pal-pdf-splitter/issues/new?template=bug_report.md)

---

**[Open Y2Pal PDF Splitter →](https://y2pal.com/split-pdf)** | **[Back to README →](https://github.com/AndrewYao93/y2pal-pdf-splitter)**
