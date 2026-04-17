---
title: "Y2Pal PDF Splitter Multi-Language Support — 5 Languages Explained"
labels: faq
---

# Y2Pal PDF Splitter Multi-Language Support

Y2Pal PDF Splitter offers interface translations in five languages: English, German, French, Japanese, and Simplified Chinese. The tool behavior is identical across languages — only the UI labels change.

## Supported Interface Languages

| Language      | Code | Subdomain        | Status     |
|---------------|------|------------------|------------|
| English       | en   | `y2pal.com`      | Default    |
| Deutsch       | de   | `de.y2pal.com`   | Full       |
| Français      | fr   | `fr.y2pal.com`   | Full       |
| 日本語        | ja   | `ja.y2pal.com`   | Full       |
| 简体中文      | zh   | `zh.y2pal.com`   | Full       |

## How Language Selection Works

### Automatic

On first visit, the browser's `Accept-Language` header is read. If it matches one of the supported languages, Y2Pal routes to the corresponding subdomain.

### Manual

A language switcher in the page header lets users override detection. The choice is stored in local storage and persists across sessions.

## Does Language Affect Processing?

No. The split operation works identically regardless of UI language:

- PDF page counts, ranges, and bookmark structures are processed the same way.
- File names are not auto-translated — a source named `contract.pdf` stays `contract.pdf`.
- Encrypted PDFs behave the same across all five languages.

## CJK and RTL Notes

- **Japanese (`ja`)**: Full UTF-8 support in file names and bookmark titles. Japanese characters in output file names are preserved correctly (no mojibake).
- **Chinese (`zh`)**: Simplified only; traditional Chinese UI is not yet offered.
- **Right-to-left languages** (Arabic, Hebrew): Not currently supported.

## What's Not Translated

- Error messages from low-level processing engines occasionally fall back to English.
- The Y2Pal blog/article content exists in English; translated articles are gradually rolled out.
- Third-party help articles linked from the tool may be English-only.

## Bookmark Titles in Output Files

When splitting by bookmark, the resulting output files take their names from the bookmark titles. If a bookmark is titled in Japanese (`第一章`), the output file is named `第一章.pdf`. The tool sanitizes file-system-illegal characters but keeps the language's native script.

## Future Languages

Language additions are considered based on user demand. Requests can be submitted via [GitHub Issues](https://github.com/AndrewYao93/y2pal-pdf-splitter/issues/new?template=feature_request.md) with expected usage volume.

## Summary

| Question                              | Answer                           |
|---------------------------------------|----------------------------------|
| Can I split PDFs in any language?     | Yes, regardless of UI language   |
| Are bookmark titles translated?       | No, original language preserved  |
| Does language affect file size caps?  | No                               |
| Does language affect daily op count?  | No                               |
| Can I switch language mid-session?    | Yes, via the header dropdown     |

---

**[Open Y2Pal PDF Splitter →](https://y2pal.com/split-pdf)** | **[Back to README →](https://github.com/AndrewYao93/y2pal-pdf-splitter)**
