---
name: web-intelligence
description: "Unified web exploration, structured data extraction, caching, and anti-bot mitigation playbook."
version: 1.0.0
author: Hermes Curator
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [web, scraping, extraction, intelligence, tavily, crawlers, api-polling]
    category: web-intelligence
---

# Web Intelligence & Search Playbook

A unified class-level playbook for conducting web scraping, search queries, multi-page crawls, and resilient data extraction while dodging cookie modals, structural blocks, and anti-bot systems.

---

## 1. Web Extraction & Search Strategy

Always map targets to the cleanest, most predictable API footprint before executing direct headless browser automation.

```
       [ Data Request ]
              │
      Is there a simple API?
       ├── YES: curl/REST (wttr.in, api queries)
       └── NO: Have explicit scrape tools (Tavily/Firecrawl)?
            ├── YES: Run Tavily search / extraction
            └── NO: fallback to browser_navigate
```

### Flow Options
- **Path A: Raw API polling / curl:** For data that exists on machine-friendly APIs (e.g. searching weather on `wttr.in`), use:
  ```bash
  curl "https://wttr.in/Paris?format=%t+%C"
  ```
- **Path B: AI-optimized intelligence proxies:** For general crawling or dynamic scrapes, use explicit Tavily/Firecrawl CLI utilities to convert messy Javascript sites into structured Markdown formats.
- **Path C: Headless Browser fallback:** Reserve full `browser_` actions (`browser_navigate`, `browser_click`, etc.) for complex UI testing, form entry steps, or sites requiring active human interaction sequences.

---

## 2. Granular Web Actions (Tavily CLI)

Use the explicitly installed Tavily CLI (`tvly` command) to execute deep searches, site mapping, or webpage content parsing.

### Custom Scrapes & Extractions
- **Advanced Search queries:**
  ```bash
  tvly search "Next-gen LLM trends 2026" --depth advanced --max-results 5 --json
  ```
- **Clean Markdown parsing:** Pull isolated body contexts without rendering sidebars, ads, or cookies:
  ```bash
  tvly extract "https://example.com/blog/article-1" --query "core architecture, benchmark metrics"
  ```
- **Website Site Mapping (Resource Discovery):** Harvest site structures to plan targeted crawls before downloading large payloads:
  ```bash
  tvly map --app "https://docs.example.com" --max-depth 2
  ```
- **Multi-page Crawford deep scans:**
  ```bash
  tvly crawl "https://docs.example.com" --limit 20 --instructions "extract API specifications only" --output-dir /tmp/api-docs/
  ```

---

## 3. Resilient Headless Recovery (Dealing with Cookie Consent & blocks)

When forced to use full browser interactions:
- **Avoid Consent dialog blocks:** Cookie banners often throw overlay dimensions that block standard clicks. If links fail to register, re-capture elements with SOM enabled (`computer_use` or `browser_snapshot`) to capture modified layouts.
- **Detect dynamic content shifts:** Pages taking >3 seconds to fully run JavaScript can record incorrect element pointers. Always pause briefly (`wait` or `sleep`) before typing or clicking.
- **Identify Bot-gate alerts:** If a page encounters CAPTCHAs, immediately alert the user or fallback to Tavily's pre-rendered APIs.
