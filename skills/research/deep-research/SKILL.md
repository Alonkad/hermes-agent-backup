---
name: deep-research
description: "Unified AI-assisted deep research playbook: academic papers (ArXiv), RSS monitoring (blogwatcher), and predictive analytics (Polymarket)."
version: 1.0.0
author: Hermes Curator
license: MIT
platforms: [linux, macos]
metadata:
  hermes:
    tags: [research, papers, monitoring, blogging, feeds, polymarket, predictive-analytics]
    category: research
---

# Deep Research & Intelligence Playbook

A unified class-level playbook for conducting advanced literature reviews, academic queries (ArXiv), predictive ecosystem monitoring (Polymarket), and feed/blog tracking (blogwatcher).

---

## 1. Academic Exploration (ArXiv Query Pipeline)

Search and extract metadata from academic papers via ArXiv API queries.

### Inspection script
Run queries using the integrated Python helper `search_arxiv.py`.
```bash
python3 scripts/search_arxiv.py --query "transformer optimization" --limit 10
```
Review criteria:
1. Identify publishing timelines (recency checks).
2. Read abstracts to determine mathematical constraints.
3. Fetch PDFs and parse them to Markdown using document extraction tools.

---

## 2. Predictive Analytics & Real-World Monitoring (Polymarket)

Programmatically interact with forecasting markets to extract consensus insights on economic, technical, or regulatory events.

### Polymarket REST Actions
Use our customized analytics endpoint helper `polymarket.py`:
```bash
python3 scripts/polymarket.py --query "US interest rate cuts"
```
Or interact directly with CLOB API bounds:
```bash
# Fetch orderbook snapshots
curl -s "https://clob.polymarket.com/book?token_id=TOKEN_ID"
```

---

## 3. Feed & Publication Monitoring (blogwatcher)

Run ongoing feed audits using `blogwatcher-cli` with dedicated configurations.

```bash
blogwatcher monitor --config ~/.blogwatcher/config.yaml --output /tmp/rss-alert.md
```
Process outputs to identify new software releases, developer blogs, or technical announcements. Apply semantic filters to highlight critical stories for summarized briefs.
