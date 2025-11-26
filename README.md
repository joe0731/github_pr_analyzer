# GitHub PR & Commit Analyzer

[中文文档](README.cn.md) | English

A powerful command-line tool for intelligently collecting, analyzing, and summarizing GitHub Pull Requests and commit records.

[![PyPI version](https://badge.fury.io/py/github-pr-analyzer.svg)](https://badge.fury.io/py/github-pr-analyzer)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🚀 Installation & Setup

### 1. Prerequisites
- **Python 3.8+**
- **Git**
- **GitHub CLI (gh)**: Must be logged in (`gh auth login`)

### 2. Install
```bash
pip install github-pr-analyzer
```

### 3. Configuration (Environment Variables)

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `CURSOR_AGENT_PATH` | Path to cursor-agent for AI features | None | **Yes** (for AI) |
| `DEFAULT_MONTHS` | Months to look back for data | `3` | No |
| `DEFAULT_REPO_PATH` | Default repository path | `.` | No |

```bash
# Example
export CURSOR_AGENT_PATH=/path/to/cursor-agent
export DEFAULT_MONTHS=6
```

## 📖 Quick Start

```bash
# 1. Interactive Mode (Best for starting)
gh-pr-analyzer interactive

# 2. Search with AI Analysis
gh-pr-analyzer search "authentication bug" --analyze

# 3. Collect Data
gh-pr-analyzer collect --save-json

# 4. Generate Daily/Weekly Report + Export Datasets
gh-pr-analyzer traverse --days 7 --save-json
gh-pr-analyzer traverse -r pytorch/pytorch --days 7 --save-json
```

All CLI workflows expose matching `--save-json` / `--no-save-json` toggles so you can enable exports when needed and opt out (for example, disable the default `view-pr` export with `--no-save-json`).

## ✨ Features
- 🔍 **Smart Search**: AI-powered keyword extraction
- 📊 **Data Collection**: PRs and merge commits statistics
- 🔄 **Diff Viewing**: Syntax-highlighted code changes
- 🤖 **AI Analysis**: Summarization via cursor-agent
- 📅 **Traverse Mode**: Batch analysis for reporting
- 🗂 **JSON Export**: Persist PR, commit, and review conversations as structured JSON

For detailed command usage, see [USAGE.md](USAGE.md).

## 🗂 JSON Export Format

All major workflows (`collect`, `search`, `traverse`, `view-pr`) share the same `--save-json` / `--no-save-json` flags (with `view-pr` defaulting to export unless `--no-save-json` is specified). Files land in `gh_pr_exports/` unless `--output-dir` is provided and follow the pattern `repo_name_<pr_num>_<pr_title>.json`.

Each JSON document contains:

- `repo`: the `owner/repo` slug used for collection
- `pr`: metadata (number, title, author, state, description, base/head refs, timestamps, URL)
- `commits`: ordered list of commits belonging to the PR with
  - `id`: full commit SHA
  - `title`: first line of the commit message
  - `message`: full commit body
  - `files`: array of `{ "path": "<file>", "diff": "<unified diff>" }`
- `conversation`: threaded review data
  - `issue_comments`: top-level PR discussion
  - `review_threads`: code review threads with inline comments and resolution state
  - `reviews`: review summaries (approve/comment/request changes)

> Example snippet:
```json
{
  "repo": "octo-org/octo-repo",
  "pr": { "number": 42, "title": "Fix login" },
  "commits": [
    {
      "id": "abc123...",
      "title": "Adjust auth flow",
      "message": "Adjust auth flow\n\n- add checks...\n",
      "files": [
        { "path": "auth/login.py", "diff": "@@ -1,3 +1,4 @@" }
      ]
    }
  ],
  "conversation": {
    "issue_comments": [],
    "review_threads": [],
    "reviews": []
  }
}
```

Use these exports to feed downstream tooling, audits, or offline review workflows.
