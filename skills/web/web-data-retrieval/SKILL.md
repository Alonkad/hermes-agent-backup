---
name: web-data-retrieval
description: Provides strategies for robust data retrieval from the web, particularly when standard browser interaction is blocked by consent forms or complex page structures.
---

# Web Data Retrieval Strategies

When attempting to retrieve data from the web, especially public information like weather forecasts, certain websites may present challenges:

- **Cookie consent dialogs:** These can block interaction and prevent direct navigation or data extraction.
- **Complex UI/UX:** Information might be embedded in dynamic content, making it hard for automated browsing tools to extract.
- **404 errors with specific URLs:** Direct navigation to presumed API endpoints or specific pages might fail.

## Preferred Workflow

1.  **Direct Browser Navigation (Initial Attempt):** Try navigating directly to a known URL that should contain the information using `browser_navigate`. Perform basic interactions if necessary (`browser_type`, `browser_press`, `browser_click`). If successful, extract the data.

2.  **Bypass Browser with CLI Tools (Fallback):** If browser interaction proves difficult (e.g., persistent cookie dialogs, unexpected page layouts), attempt to retrieve data using command-line tools like `curl` with a suitable API or specialized service.

    -   **Identify potential data sources:** Look for simplified web services or APIs that provide the required information in a machine-readable format (e.g., JSON, plain text).
    -   **Use `curl`:** Construct a `curl` command to fetch the data. Example: `curl "https://wttr.in/Herzliya?format=%t+%C"` for weather.
    -   **Process output:** Use `execute_code` with Python's `json` module or string manipulation to parse the `curl` output.

## Pitfalls

-   **Over-reliance on `browser` tools for simple data:** For plain text, JSON, or easily parseable content, `curl` or `web_extract` are often more efficient and reliable than full browser simulation.
-   **Ignoring `wttr.in`:** For weather information, `wttr.in` is a highly reliable and simple command-line tool. Always try `curl "https://wttr.in/<location>?format=<format_string>"` before resorting to complex browser navigation for weather.
-   **Getting stuck in consent loops:** If a website continuously presents cookie consent forms even after attempts to accept them, switch to a CLI-based approach if possible.

## Verification

-   Always verify the extracted data against common sense or another source if available.
-   Ensure the CLI command works reliably and returns the expected format.
