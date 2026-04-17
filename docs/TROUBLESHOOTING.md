# Y2Pal PDF Splitter Troubleshooting Guide

> Solutions to common issues. Can't find your answer?
> [Open a support issue →](https://github.com/AndrewYao93/y2pal-pdf-splitter/issues/new?template=bug_report.md)

[← Back to README](../README.md)

---

## Table of Contents

- [Upload Issues](#upload-issues)
- [Split Processing Issues](#split-processing-issues)
- [Download Issues](#download-issues)
- [Compatibility Issues](#compatibility-issues)
- [Access & Account Issues](#access--account-issues)
- [Privacy & Security Issues](#privacy--security-issues)

---

## Upload Issues

### Upload stalls near the end or times out

**Symptoms:** Progress bar stops at 90-99% and never finishes; browser eventually throws a network error.

**Solutions:**
1. Check the free-tier file-size cap on the page header — the server rejects oversized files after the POST completes.
2. Verify upload bandwidth. `≥ 2 Mbps` is recommended; large PDFs over mobile hotspot often fail.
3. Try a wired or standard Wi-Fi connection; captive portals (hotels, airports) sometimes cap POST payload size.
4. Disable browser extensions (ad blockers, privacy suites) — they occasionally break multipart uploads.
5. If over 500 MB, split the PDF locally first with a desktop tool and upload the pieces.

### Drag-drop doesn't activate the drop zone

**Symptoms:** Dragging a file over the page does nothing; zone doesn't highlight.

**Solutions:**
1. Make sure the file is a `.pdf` — other formats are rejected at the drag-enter event.
2. Click the drop zone and use the file picker as a fallback.
3. In Safari, check that drag-drop is enabled in preferences.
4. On Linux + Firefox with Wayland, drag from a file manager may not forward the MIME type — use the picker.

### "File rejected" error immediately on upload

**Symptoms:** Upload fails within a second of starting.

**Solutions:**
1. Confirm the file is a valid PDF. Try opening it locally — if the native reader refuses, the file is corrupt.
2. Check that the file extension is `.pdf` (not `.PDF ` with a trailing space from macOS Finder rename).
3. If the PDF is XFA-only (form-heavy legacy format), convert to standard PDF first.

---

## Split Processing Issues

### Output has wrong page count

**Symptoms:** A range of `1-5` returns an output with 4 pages or 6 pages.

**Solutions:**
1. Verify page numbering. PDF page indices are 1-based in Y2Pal's UI — `1-5` means pages 1, 2, 3, 4, 5 inclusive.
2. Check the source's front-matter. Scanned books sometimes start page 1 after the cover; the splitter uses absolute page positions, not the printed page number.
3. Re-check the range syntax: use commas to separate distinct ranges, hyphens for ranges, single numbers for single pages.

### Bookmark split detects no bookmarks

**Symptoms:** The bookmark mode is disabled or shows "no bookmarks detected" even though the PDF has a TOC.

**Solutions:**
1. The PDF may have a visual TOC (text on a page) rather than structural bookmarks. Open it in Adobe Reader and check the Bookmarks pane — if empty there, Y2Pal cannot extract them.
2. Add bookmarks with a desktop editor (Adobe Acrobat, PDFescape, Foxit) and re-upload.
3. Fall back to page-range mode with manually noted chapter start pages.

### Output PDFs lose formatting or render differently

**Symptoms:** Fonts substitute, images shift, or form fields appear blank.

**Solutions:**
1. Confirm the source renders correctly in Chrome's built-in PDF viewer before splitting.
2. If fonts are embedded as subsets per page, the splitter preserves them — but very old readers may still substitute. Update the reader.
3. For PDFs with flattened annotations, use the "flatten before split" pre-processing option if available; otherwise flatten locally.
4. Report the source PDF producer string (Adobe InDesign, LibreOffice, etc.) in a [GitHub Issue](https://github.com/AndrewYao93/y2pal-pdf-splitter/issues) for reproducible diagnosis.

---

## Download Issues

### "Download All" zip is empty or corrupted

**Symptoms:** The zip downloads but contains 0 files or refuses to open.

**Solutions:**
1. Retry the zip generation — transient S3 / storage glitches usually recover on retry.
2. Download each output file individually as a workaround.
3. Check that the browser isn't auto-extracting and deleting the zip (Safari has this on by default).
4. If the zip is flagged as unsafe by the OS, unblock it in file properties.

### Individual file downloads trigger "unsafe download" warning

**Symptoms:** Chrome or Edge warns that the file "may be dangerous."

**Solutions:**
1. This is a generic Chromium warning for any downloaded PDF; it does not indicate malicious content.
2. Click "Keep" in the download shelf to proceed.
3. On corporate machines, ask IT to allowlist `y2pal.com` downloads.

### Download saved with generic filename

**Symptoms:** Files are named `download.pdf`, `download (1).pdf` instead of descriptive names.

**Solutions:**
1. This happens when the browser strips the `Content-Disposition` header (some iOS browsers do). Rename manually after download.
2. Use the desktop browser for workflow-critical naming.

---

## Compatibility Issues

### Tool doesn't load on iOS Safari

**Symptoms:** Blank white page or spinning indicator that never resolves.

**Solutions:**
1. Update iOS to 14 or newer — earlier versions lack required JS APIs.
2. Disable the "Prevent Cross-Site Tracking" option for `y2pal.com` if it interferes with the upload.
3. Try Chrome on iOS as a fallback.
4. Clear Safari data: Settings → Safari → Clear History and Website Data.

### Tool blocked by corporate proxy or firewall

**Symptoms:** Page loads but uploads fail with CORS or 403 errors.

**Solutions:**
1. Confirm outbound HTTPS to `*.y2pal.com` is allowlisted on the corporate firewall.
2. Some deep-packet-inspection proxies strip multipart boundaries; request a direct route or use a personal hotspot as a diagnostic.
3. If working from a SaaS security gateway (Zscaler, Netskope), submit a policy exception with your IT team.

### No output on Firefox with strict Enhanced Tracking Protection

**Symptoms:** Page loads but the split button is greyed out after upload.

**Solutions:**
1. Click the shield icon in the address bar and disable protection for `y2pal.com`.
2. Alternatively, switch to Chromium-based browser for this session.

---

## Access & Account Issues

### Free-tier limit reached mid-day

**Symptoms:** After several uploads, the splitter refuses with a "daily limit reached" notice.

**Solutions:**
1. Free-tier daily counts reset at UTC midnight. Wait or schedule workloads earlier.
2. Upgrade to a lifetime license for unlimited processing — see the [product page](https://y2pal.com/split-pdf).

### Lifetime license not recognized on another device

**Symptoms:** Upgrade purchased on one browser but another browser / device still sees free-tier caps.

**Solutions:**
1. Y2Pal ties the license to the purchase email. Sign in with the same email on the other device.
2. If sign-in is not available yet (early rollout), contact support at `contact@y2pal.com` with the order ID.

### Email confirmation never arrives

**Symptoms:** Upgrade flow sends a confirmation email that never shows up.

**Solutions:**
1. Check spam / promotions folders first.
2. Gmail occasionally sends DVDFab-family emails to "Updates". Move one to inbox to train the filter.
3. Contact `contact@y2pal.com` with the order ID for a resend.

---

## Privacy & Security Issues

### Concern: Where is my PDF stored?

**Answer:** Uploaded PDFs are held in Y2Pal's temporary processing bucket for the duration of the session and removed after processing completes. They are not indexed, not shared, not backed up long-term. Transfers use HTTPS with TLS 1.3.

### Concern: Is my password to an encrypted PDF stored?

**Answer:** No. Passwords are used in-memory for the decryption step and are not written to disk, not logged, and not transmitted beyond the processing worker.

### Concern: Can I use this tool with regulated data (HIPAA, GDPR, etc.)?

**Solutions:**
1. Y2Pal's free tier is not HIPAA-certified; do not upload PHI without a signed BAA.
2. GDPR-covered data transit is in-scope — see the privacy policy at `y2pal.com/privacy-policy` for data-handling details.
3. For regulated workflows, a self-hosted split workflow using local tools is safer.

### Concern: Does Y2Pal use uploaded PDFs for AI training?

**Answer:** No. Y2Pal does not extract, sample, index, or train on user uploads.

---

## Still Need Help?

- [Open a GitHub Issue](https://github.com/AndrewYao93/y2pal-pdf-splitter/issues/new?template=bug_report.md)
- Y2Pal support email: `contact@y2pal.com`

---

[← Back to README](../README.md)
