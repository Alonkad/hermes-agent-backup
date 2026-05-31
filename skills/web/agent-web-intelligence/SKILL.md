---
name: agent-web-intelligence
description: Provides strategies and workflows for AI agents to effectively search, browse, and extract structured information from the web, bypassing common challenges like anti-bot measures and cookie consents.
---

# Agent Web Intelligence

This skill outlines an enhanced approach for an AI agent to interact with the web for information retrieval, moving beyond basic `browser_navigate` for general search tasks.

## Challenges with Direct Browser Interaction for Search

Directly using `browser_navigate`, `browser_type`, and `browser_click` for web searching (e.g., Google, Weather.com) often leads to:
-   **Cookie Consent Dialogs:** Many websites present mandatory cookie consent forms that require interaction, leading to extra steps and potential loops.
-   **Aggressive Bot Detection:** Search engines and other dynamic websites may employ CAPTCHAs or block access when automated browsing is detected, especially without residential proxies.
-   **Unstructured Data:** Information on general websites is often not in a structured format suitable for direct AI consumption, requiring complex parsing or vision-based interpretation.
-   **HTTP Errors:** Direct navigation to specific URLs can sometimes result in `net::ERR_HTTP_PROTOCOL_ERROR` or 404s, especially when constructing URLs with search terms.

## Preferred Workflow for Web Information Retrieval

1.  **Prioritize Dedicated APIs for Structured Search/Scraping:**
    *   For general web search (titles, snippets, URLs), prefer integrating a dedicated search API (e.g., Serper.dev, SerpApi.com). These services return structured JSON data, bypassing browser interaction complexities.
    *   For sophisticated page scraping and interaction with dynamic content, consider services like Firecrawl.dev. These APIs normalize web content into AI-friendly formats (JSON, Markdown) and handle anti-bot measures, JavaScript rendering, and direct interaction (clicks, form fills) via API calls.

2.  **Use `curl` for Simple, Machine-Readable APIs:**
    *   For straightforward queries to APIs that return plain text or simple JSON (e.g., `wttr.in` for weather), use the `terminal` tool with `curl`. This is efficient and avoids browser overhead.
    *   Example: `curl "https://wttr.in/Herzliya?format=%t+%C"`

3.  **Strategic Browser Use for Interactive Tasks/Documentation:**
    *   Reserve `browser_navigate`, `browser_type`, `browser_click`, and `browser_snapshot` for tasks that genuinely require interaction with web applications (e.g., filling forms, clicking specific UI elements, testing a web UI, or directly reading documentation pages that are hard to get from APIs).
    *   If using the browser for documentation, navigate directly to the API/docs page rather than searching through a general search engine, to avoid intermediate steps.

## Integrating New Web Intelligence Tools

When a new web intelligence tool (like Firecrawl.dev) is identified:
1.  **Consult Documentation:** Navigate directly to the tool's documentation (e.g., `firecrawl.dev/docs`) using `browser_navigate`.
2.  **Identify API Endpoints and Authentication:** Understand how to make API calls (REST, GraphQL) and how to authenticate (API keys, tokens).
3.  **Test with `terminal` (for `curl`) or `execute_code` (for Python SDKs):** Perform initial tests to ensure connectivity and correct response parsing.
4.  **Create a New Skill:** Encapsulate the interaction logic for the new tool into a dedicated skill, making it reusable and robust.

This approach ensures more reliable, efficient, and structured web information gathering for AI agents.
