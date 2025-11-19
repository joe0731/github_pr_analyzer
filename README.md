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
gh-pr-analyzer collect

# 4. Generate Daily/Weekly Report
gh-pr-analyzer traverse --days 7
gh-pr-analyzer traverse -r pytorch/pytorch --days 7
```

## ✨ Features
- 🔍 **Smart Search**: AI-powered keyword extraction
- 📊 **Data Collection**: PRs and merge commits statistics
- 🔄 **Diff Viewing**: Syntax-highlighted code changes
- 🤖 **AI Analysis**: Summarization via cursor-agent
- 📅 **Traverse Mode**: Batch analysis for reporting

For detailed command usage, see [USAGE.md](USAGE.md).
