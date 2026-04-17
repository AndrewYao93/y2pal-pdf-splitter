---
title: "Y2Pal PDF Splitter Browser Compatibility Guide — Supported Browsers"
labels: faq
---

# Y2Pal PDF Splitter Browser Compatibility Guide

Y2Pal PDF Splitter runs in the browser — which means the browser version matters. Here's the full compatibility matrix and what to do if your browser isn't supported.

## Minimum Browser Versions

| Browser          | Minimum | Fully Tested | Notes                               |
|------------------|---------|--------------|-------------------------------------|
| Google Chrome    | 90      | Latest stable| All platforms                       |
| Mozilla Firefox  | 88      | Latest stable| Adjust strict tracking protection   |
| Apple Safari     | 14      | Latest stable| macOS 11+ / iOS 14+                 |
| Microsoft Edge   | 90      | Latest stable| Chromium-based only; not legacy Edge|
| Opera            | 76      | Latest stable| Chromium-based                      |
| Brave            | 1.20    | Latest stable| Disable shield for file upload      |
| Vivaldi          | 3.7     | Latest stable| Chromium-based                      |
| Samsung Internet | 14      | Latest stable| Android only                        |

## Not Supported

- Internet Explorer (any version).
- Legacy Microsoft Edge (pre-Chromium, 2015-2020).
- Chrome / Firefox versions older than the minimum above.
- Text-only browsers (Lynx, w3m, elinks).

## What If My Browser Is Unsupported?

### Option 1: Update the Browser

All listed browsers offer free updates to the latest version from their official sites:

- Chrome: `chrome://settings/help`
- Firefox: `about:preferences` → "Firefox Updates"
- Safari: macOS System Settings → General → Software Update
- Edge: `edge://settings/help`

### Option 2: Use a Different Browser

If the primary browser is locked (corporate managed, older OS), install a second browser that meets the minimum. Portable versions of Firefox and Chrome are available for this use case.

### Option 3: Use a Different Device

If the current device can't run a supported browser, switch to a phone, tablet, or another computer that can.

## Operating System Requirements

Supported browsers run on:

| OS                 | Supported Version            |
|--------------------|------------------------------|
| Windows            | 10 / 11                      |
| macOS              | 11 Big Sur or later          |
| iOS / iPadOS       | 14 or later                  |
| Android            | 10 or later                  |
| ChromeOS           | Current                      |
| Ubuntu / Fedora / Debian | Any recent version     |

Older OS versions can still run if they support one of the listed browsers — but in practice, older OSs cap browser versions well below Y2Pal's requirements.

## JavaScript & Cookies

- **JavaScript**: Required. Disabled-JavaScript fallback is not provided.
- **Cookies**: Session cookies required; third-party cookies not used.
- **Local storage**: Used for UI preferences only (language, last-used split mode).

## Privacy-Focused Browsers (Tor, Brave, LibreWolf)

These browsers work, but strict shields sometimes block multipart upload or drag-drop. If the tool behaves oddly:

1. Click the shield icon in the address bar.
2. Lower protection for `y2pal.com` to "standard".
3. Retry the action.

No sensitive user data is tracked by the page; dropping the shield for this domain is acceptable.

## Report Compatibility Issues

If you're using a supported browser and something still doesn't work:

- [Open a bug report →](https://github.com/AndrewYao93/y2pal-pdf-splitter/issues/new?template=bug_report.md)
- Include browser name, exact version, OS, and the specific step that fails.

---

**[Open Y2Pal PDF Splitter →](https://y2pal.com/split-pdf)** | **[Back to README →](https://github.com/AndrewYao93/y2pal-pdf-splitter)**
