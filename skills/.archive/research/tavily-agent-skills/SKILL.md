---
name: tavily-agent-skills
description: "Utilize advanced Tavily web research and extraction skills for more efficient and targeted information gathering."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux]
metadata:
  tavily:
    skills_installed: true
    cli_installed: true
    security_warning_reviewed: true
tags: [web-search, research, tavily, extraction, crawling, data-science]
---

# Tavily Agent Skills

This skill document outlines the capabilities provided by the dedicated Tavily Agent Skills that have been installed on this Hermes Agent instance. These skills offer more granular control and advanced functionalities for web research, content extraction, and site crawling compared to the generic `web_search` tool.

**Note:** The `web_search` tool implicitly uses Tavily as its backend. This skill focuses on explicitly leveraging the specialized Tavily CLI-based functions.

## Installation Status

The Tavily CLI and the following 8 Tavily Agent Skills have been successfully installed:

*   `tavily-best-practices`
*   `tavily-cli`
*   `tavily-crawl`
*   `tavily-dynamic-search`
*   `tavily-extract`
*   `tavily-map`
*   `tavily-research`
*   `tavily-search`

**Important: Agent Restart Required!**
For these newly installed skills to be fully active and available for use, the Hermes Agent process (or this session) needs to be restarted.

## Available Tavily Agent Skills and Their Purpose

Here's an overview of the core Tavily skills now at my disposal:

*   **`tavily-search`**:
    *   **Purpose:** Performs highly customized web searches.
    *   **Key Options:** `--depth` (ultra-fast/fast/basic/advanced), `--max-results`, `--topic`, `--time-range`, `--include-domains`, `--exclude-domains`, `--include-raw-content`.
    *   **Use Case:** When a precise search with specific filtering or depth is required.

*   **`tavily-extract`**:
    *   **Purpose:** Extracts clean markdown or text content from one or more URLs.
    *   **Key Options:** `--query` (for focused extraction), `--chunks-per-source`, `--extract-depth` (basic/advanced), `--format` (markdown/text).
    *   **Use Case:** To get summary or specific information directly from web pages, especially dynamically rendered ones.

*   **`tavily-crawl`**:
    *   **Purpose:** Crawls an entire website to extract content from multiple pages.
    *   **Key Options:** `--max-depth`, `--limit`, `--instructions` (for semantic filtering), `--chunks-per-source`, `--output-dir`, `--select-paths`, `--exclude-paths`.
    *   **Use Case:** For comprehensive data collection from a specific website following certain criteria.

*   **`tavily-map`**:
    *   **Purpose:** Discovers and lists all URLs on a website without extracting content.
    *   **Key Options:** `--max-depth`, `--limit`, `--instructions` (for URL filtering), `--select-paths`, `--exclude-paths`.
    *   **Use Case:** To pre-identify relevant URLs before performing extraction or crawling.

*   **`tavily-research`**:
    *   **Purpose:** Conducts AI-powered deep research, gathering sources, analyzing them, and producing a cited report.
    *   **Key Options:** `--model` (mini/pro/auto), `--stream`, `--citation-format`, `--output-schema`, `-o` (output file).
    *   **Use Case:** For in-depth analysis and synthesis of information from multiple web sources, leading to a structured report.

*   **`tavily-cli`, `tavily-dynamic-search`, `tavily-best-practices`**: These are supporting skills for broader usage, dynamic search variations, and best practices guidance.

## Usage Guidelines

To explicitly invoke these skills, I need to use the Tavily CLI commands directly via the `terminal` tool. For example:

```bash
tvly search "latest AI trends" --depth advanced --max-results 5 --json
```

Or for extraction:

```bash
tvly extract "https://example.com/article" --query "key findings"
```

The Hermes Agent may also automatically invoke these skills based on natural language prompts if it determines they are the most appropriate tools for the task.

## Security Considerations

During the installation, a security scan identified several of these skills with "Critical Risk" according to Snyk. While the specific nature of these risks (e.g., outdated dependencies, potential vulnerabilities) is not immediately detailed within the `skills add` output, it is crucial to be aware of this. Further investigation into these risks (e.g., by visiting `https://skills.sh/tavily-ai/skills`) is recommended for responsible usage. I will exercise caution when using skills flagged with higher risks.

## Future Enhancements

This new skill will enable more precise and powerful web interaction. I can now:
*   Conduct more targeted searches using parameters like search depth and domain filtering.
*   Extract specific content from web pages efficiently.
*   Crawl websites for comprehensive data.
*   Perform deep research and generate cited reports.
