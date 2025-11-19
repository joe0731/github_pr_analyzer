# GitHub PR & Commit Analyzer - Project Overview

[中文文档](PROJECT_OVERVIEW.cn.md) | English

## Project Introduction

GitHub PR & Commit Analyzer is a production-grade command-line tool for intelligently collecting, analyzing, and summarizing GitHub Pull Requests and commit records.

**Version**: 3.0.4  
**PyPI**: `github-pr-analyzer`

## Technical Architecture

### Architecture Design

```
┌─────────────────────────────────────────────────────────┐
│               CLI Interface (gh-pr-analyzer)            │
│  - Command parsing (Click)                              │
│  - User interaction (Rich)                              │
└──────────────┬──────────────────────────────────────────┘
               │
        ┌──────┴───────┐
        │              │
┌───────▼──────┐  ┌───▼──────────┐
│ PR Collector │  │Commit Collec.│
│ (gh CLI)     │  │ (GitPython)  │
└──────┬───────┘  └───┬──────────┘
       │              │
       └──────┬───────┘
              │
       ┌──────▼───────┐
       │   Matcher    │
       │ (Fuzzy/AI)   │
       └──────┬───────┘
              │
    ┌─────────┴─────────┐
    │                   │
┌───▼─────────┐  ┌──────▼────────┐
│ Diff Viewer │  │  AI Analyzer  │
└─────────────┘  └───────────────┘
```

### Modules

- **src/cli.py**: Entry point (`gh-pr-analyzer`), handles commands (`search`, `collect`, `traverse`, etc.).
- **src/pr_collector.py**: Wraps GitHub CLI (`gh`) to fetch PR data.
- **src/commit_collector.py**: Uses GitPython to inspect local git history.
- **src/matcher.py**: Implements fuzzy search and AI keyword extraction.
- **src/ai_analyzer.py**: Integrates with external `cursor-agent` for LLM analysis.
- **src/diff_viewer.py**: Renders syntax-highlighted diffs.

## Dependencies

- **Python 3.8+**
- **Git** & **GitHub CLI (gh)**
- **Python Packages**: `click`, `rich`, `requests`, `gitpython`, `fuzzywuzzy`, `python-levenshtein`, `python-dateutil`
