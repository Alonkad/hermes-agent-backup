---
name: github-playbook
description: "Unified GitHub operational playbook: authentication, codebase inspections, issues, PR workflows, code reviews, and repo-management."
version: 1.0.0
author: Hermes Curator
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [GitHub, Automation, Auth, Code-Review, Issues, Pull-Requests, Repositories]
    category: github
---

# GitHub Unified Playbook

A unified class-level playbook for integrating, managing, and automating repository workflows on GitHub. This playbook guides checking authentication, inspecting codebases, performing security-focused reviews, managing issues, constructing pull requests, triggering CI, and controlling repository settings.

---

## 1. Authentication Configuration

Always check current authentication states before attempting remote operations.

### Quick Auth Detection Flow
Use this step to check if `gh` CLI or `git` with tokens/keys is available:
```bash
if command -v gh &>/dev/null && gh auth status &>/dev/null; then
  export AUTH_METHOD="gh"
elif [ -n "$GITHUB_TOKEN" ]; then
  export AUTH_METHOD="curl"
elif [ -f ~/.hermes/.env ] && grep -q "^GITHUB_TOKEN=" ~/.hermes/.env; then
  export GITHUB_TOKEN=$(grep "^GITHUB_TOKEN=" ~/.hermes/.env | head -1 | cut -d= -f2 | tr -d '\n\r')
  export AUTH_METHOD="curl"
elif grep -q "github.com" ~/.git-credentials 2>/dev/null; then
  export GITHUB_TOKEN=$(grep "github.com" ~/.git-credentials | head -1 | sed 's|https://[^:]*:\([^@]*\)@.*|\1|')
  export AUTH_METHOD="curl"
else
  export AUTH_METHOD="none"
fi
```

### Setup Methods
- **Method 1: Git-Only HTTPS (Token):** Tell user to generate a Classic Token scope (`repo`, `workflow`, `read:org`) on **https://github.com/settings/tokens**. Run:
  ```bash
  git config --global credential.helper store
  # Next action triggers verification; enter username and paste TOKEN as password.
  git ls-remote https://github.com/owner/repo.git
  ```
- **Method 2: SSH Key Setup:**
  ```bash
  ssh-keygen -t ed25519 -C "their-email@example.com" -f ~/.ssh/id_ed25519 -N ""
  cat ~/.ssh/id_ed25519.pub
  ```
  Instruct user to paste it on **https://github.com/settings/keys**.
- **Method 3: gh CLI:** Install and authorize using `gh auth login` (or automated token piping: `echo "$TOKEN" | gh auth login --with-token`).

---

## 2. Codebase Inspection (pygount)

Assess repository metrics, file counts, and documentation ratios using line of code analyzers.

### Basic Inspection Command
Exclude build artifacts and dependencies to prevent hangs or processing loops:
```bash
pygount --format=summary \
  --folders-to-skip=".git,node_modules,venv,.venv,__pycache__,.cache,dist,build,.next,.tox" \
  .
```

---

## 3. GitHub Issues Triage & Management

Create, search, list, assign, and transition issue tickets.

- **Create via gh:**
  ```bash
  gh issue create --title "Redirect Bug" --body "$(cat templates/bug-report.md)" --label "bug" --assignee "@me"
  ```
- **Create via curl:**
  ```bash
  curl -s -X POST -H "Authorization: token $GITHUB_TOKEN" \
    https://api.github.com/repos/$OWNER/$REPO/issues \
    -d "{\"title\":\"Redirect Bug\", \"body\":\"Details...\", \"labels\":[\"bug\"]}"
  ```
- **Transition state:** Use keywords like `Closes #123`, `Fixes #123`, or `Resolves #123` in commits or PR summaries to handle auto-closing upon branch merges.

---

## 4. Pull Request Lifecycles & Workflow

Coordinate development lifecycles from branch creation to merging.

1. **Local branching:**
   ```bash
   git checkout main && git pull origin main
   git checkout -b feat/add-user-authentication
   ```
2. **Pushing:**
   ```bash
   git push -u origin HEAD
   ```
3. **Establishing PR:**
   - **gh CLI:** `gh pr create --title "feat: auth" --body "Summary" --draft`
   - **REST API:** POST definitions to `/repos/$OWNER/$REPO/pulls`.
4. **CI Checks Tracking:**
   - **gh CLI:** `gh pr checks --watch`
   - **Curl polling loops:** Poll combined statuses on `/repos/$OWNER/$REPO/commits/$SHA/status`.
5. **Merging:**
   - **gh CLI:** `gh pr merge --squash --delete-branch`
   - **REST API:** PUT squash payloads to `/pulls/$PR_NUMBER/merge`.

---

## 5. Structured Code Reviews

Systematically assess additions, local branches, or foreign PRs against security and performance baselines.

### Local (Pre-Commit) Checking
Verify staged index configurations prior to push operations:
```bash
git diff --cached
```
Check for common problems:
- Hardcoded keys (API endpoints, credentials, secrets)
- Command injection vectors (`subprocess.run(shell=True)`)
- Execution blocks (`eval()`, `exec()`, `pickle.loads()`)
- Unparameterized database formats

### Remote PR Commenting
Leave bulk inline code comments concurrently:
```bash
curl -s -X POST -H "Authorization: token $GITHUB_TOKEN" \
  https://api.github.com/repos/$OWNER/$REPO/pulls/$PR_NUMBER/reviews \
  -d "{
    \"commit_id\": \"$HEAD_SHA\",
    \"event\": \"REQUEST_CHANGES\",
    \"body\": \"Review feedback summary.\",
    \"comments\": [
      {\"path\": \"src/auth.py\", \"line\": 42, \"body\": \"🔴 Use parameterized query.\"}
    ]
  }"
```

---

## 6. Repository Administration & Settings

Manage webhooks, secrets, releases, and branch protection models.

- **Releases (gh):** `gh release create v1.0.0 --generate-notes`
- **Secrets Encryption (gh):** `gh secret set DB_PASS --body "secret_string"`
- **Branch Protection rules:** PUT restriction schemas containing rules to `/branches/main/protection` to mandate approvals or status checks.
