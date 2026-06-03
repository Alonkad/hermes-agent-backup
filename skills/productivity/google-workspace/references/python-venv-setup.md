# Python Virtual Environment Setup for Google Workspace Skill

This document explains how to set up a Python virtual environment to install the necessary dependencies for the Google Workspace skill when running in an externally managed Python environment.

## Problem

In some Linux distributions or managed environments, direct installation of Python packages system-wide using `pip install` fails due to environment restrictions (e.g., `externally-managed-environment` errors).

## Solution

1. **Create a dedicated virtual environment for the skill dependencies:**

```bash
python3 -m venv ~/.hermes/.venv_google_workspace
```

2. **Activate the virtual environment:**

```bash
source ~/.hermes/.venv_google_workspace/bin/activate
```

3. **Install required Python packages inside the virtual environment:**

```bash
pip install google-api-python-client google-auth google-auth-httplib2 google-auth-oauthlib
```

4. **Run the skill's Python scripts using the virtual environment's python:**

```bash
~/.hermes/.venv_google_workspace/bin/python3 ~/.hermes/skills/productivity/google-workspace/scripts/google_api.py calendar list
```

## Notes

- Always use the Python executable from the virtual environment to ensure dependencies are available.
- This avoids polluting the system Python and complies with environment restrictions.

## Added to Google Workspace skill
This reference is linked from the main skill's documentation to guide future troubleshooting and setup.
