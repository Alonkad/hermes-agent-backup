## Claude Code Settings reference

### Typical `~/.claude/settings.json` format:

```json
{
  "theme": "dark",
  "autoDreamEnabled": true,
  "assistant": true,
  "telemetry": false,
  "autoPlanning": "smart",
  "hooks": {
    "pre-commit": "npm run test"
  }
}
```

### Config File Paths by OS:
- **macOS**: `~/Library/Application Support/ClaudeCode/settings.json`
- **Linux/WSL**: `~/.config/ClaudeCode/settings.json` (user-level) or `~/.claude/settings.json`
- **Windows**: `%APPDATA%\ClaudeCode\settings.json`

### Memory Directory Structure:
```text
~/.claude/projects/<project-id>/
├── memory/
│   ├── MEMORY.md            # Startup index (Max 200 lines)
│   ├── build.md             # Custom topic file for compilation notes
│   ├── tests.md             # Topic memory for test executions
│   └── logs/
│       └── 2026/
│           └── 06/
│               └── 2026-06-10.md    # Append-only daily log entry stream
├── sessions/
│   ├── session-1.jsonl      # Interactive history 
│   └── session-2.jsonl
└── .consolidate-lock        # Auto-dream run prevention lock
```

### Advanced GrowthBook Flags:
- `tengu_onyx_plover`: Triggers the Auto-Dream rollout status.
- `tengu_kairos`: Controls background persistence client daemon.
