# Change Log

All notable changes to the VPS Configuration and Service states are documented here.

## [2026-06-12]
- **Documented Serving Patterns:** Populated `references/dashboard-caddy-dns.md` with complete documentation on how to serve static, fully interactive HTML files under the `/assets` build-mount of the FastAPI dashboard on port 9119. 
- **Bypassed Basic Auth on Mobile:** Documented the URL-embedded basic authentication recipe using `@62.238.18.137` to allow friction-free access to interactive files on phones/tablets for the family without popup prompts.

## [2026-06-11]
- **Analyzed:** Diagnosed a brief gateway disconnect. Discovered it was a graceful reload (SIGTERM) triggered by an automatic upgrade of `openssl`/`libssl3t64` by Debian/Ubuntu package manager (`unattended-upgrades`).
- **Added:** Added `references/operations.md` to document diagnostic commands for analyzing gateway logs and system-initiated service restarts (such as library upgrades).
