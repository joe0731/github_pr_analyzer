# GitHub PR & Commit Analyzer - Project Overview

[中文文档](PROJECT_OVERVIEW.cn.md) | English

## Project Introduction

GitHub PR & Commit Analyzer is a production-grade command-line tool for intelligently collecting, analyzing, and summarizing GitHub Pull Requests and committed merge commits. The tool supports keyword-based smart search and can integrate with AI (cursor-agent CLI) for in-depth analysis.

## Core Features

### 1. Data Collection
- ✅ Collect all open Pull Requests
- ✅ Collect merged Pull Requests within specified time range (default 3 months)
- ✅ Collect merge commits from Git repository
- ✅ Auto-detect current repository or manually specify
- ✅ Support dual-source collection from GitHub API and local Git repository

### 2. Smart Search
- ✅ Fuzzy matching search based on keywords
- ✅ Multi-field search (title, description, author, labels, commit message)
- ✅ Smart scoring system (0-100 points)
- ✅ Configurable minimum match score and result count
- ✅ Support single and multiple keyword combination search

### 3. Diff Viewing
- ✅ Complete code change diff viewing
- ✅ Color syntax highlighting
- ✅ Support PR diff and commit diff
- ✅ File list display
- ✅ Configurable display line limits

### 4. AI Analysis
- ✅ Integration with cursor-agent CLI for intelligent analysis
- ✅ Automatic summarization of change purpose and impact
- ✅ Technical implementation detail analysis
- ✅ Impact scope and risk assessment
- ✅ Batch analysis of multiple PRs/commits
- ✅ Generate Markdown format analysis reports

### 5. User Interface
- ✅ Beautiful terminal output (using Rich library)
- ✅ Interactive command-line mode
- ✅ Multiple subcommands for different operations
- ✅ Progress indicators and status prompts
- ✅ Color-coded result display
- ✅ Tabulated search results

## Technical Architecture

### Architecture Design

```
┌─────────────────────────────────────────────────────────┐
│                    CLI Interface (cli.py)               │
│  - Command parsing and user interaction                 │
│  - Progress display and result formatting               │
└──────────────┬──────────────────────────────────────────┘
               │
        ┌──────┴───────┐
        │              │
┌───────▼──────┐  ┌───▼──────────┐
│ PR Collector │  │Commit Collec.│
│              │  │              │
│ - GitHub API │  │ - GitPython  │
│ - gh CLI     │  │ - Local repo │
└──────┬───────┘  └───┬──────────┘
       │              │
       └──────┬───────┘
              │
       ┌──────▼───────┐
       │   Matcher    │
       │              │
       │ - Fuzzy match│
       │ - Scoring    │
       └──────┬───────┘
              │
    ┌─────────┴─────────┐
    │                   │
┌───▼─────────┐  ┌──────▼────────┐
│ Diff Viewer │  │  AI Analyzer  │
│             │  │               │
│ - Syntax HL │  │ - cursor-agent│
│ - File list │  │ - Report gen  │
└─────────────┘  └───────────────┘
```

### Module Description

#### src/config.py
- Configuration management
- Environment variable loading
- Configuration validation

#### src/utils.py
- Common utility functions
- Command execution wrapper
- Date processing
- Dependency checking

#### src/pr_collector.py
- Pull Request collection
- GitHub API interaction
- gh CLI invocation
- PR data model

#### src/commit_collector.py
- Git commit collection
- GitPython operations
- Merge commit detection
- Commit data model

#### src/diff_viewer.py
- Code change viewing
- Diff generation and formatting
- Syntax highlighting
- File comparison

#### src/matcher.py
- Smart search and matching
- Fuzzy matching algorithm
- Scoring system
- Multiple keyword handling

#### src/ai_analyzer.py
- AI analysis integration
- cursor-agent invocation
- Prompt generation
- Report generation

#### src/cli.py
- Command-line interface
- Subcommand implementation
- Interactive mode
- Result display

## Dependencies

### Core Dependencies
- **Python 3.8+**: Programming language
- **Git**: Version control system
- **GitHub CLI (gh)**: GitHub API access
- **cursor-agent**: AI analysis (optional)

### Python Packages
- **click**: CLI framework
- **rich**: Terminal beautification
- **GitPython**: Git operations
- **requests**: HTTP requests
- **python-dotenv**: Environment variables
- **fuzzywuzzy**: Fuzzy matching
- **python-levenshtein**: String distance
- **python-dateutil**: Date processing

## Use Cases

### Scenario 1: Release Management
```bash
# Collect recent changes
python main.py collect --months 1

# Search for new features
python main.py search "feature" --analyze

# Search for bug fixes
python main.py search "fix" --analyze

# Generate release notes foundation
```

### Scenario 2: Code Review
```bash
# View specific PR
python main.py view-pr 123 --analyze

# Deep dive into:
# - PR purpose
# - Code changes
# - Potential impact
```

### Scenario 3: Security Audit
```bash
# Search security-related changes
python main.py search "security vulnerability CVE" \
  --months 6 \
  --analyze

# Generate security change report
```

## Project Characteristics

### 1. Production Quality
- ✅ Complete error handling and exception management
- ✅ Detailed logging and status prompts
- ✅ Input validation and security checks
- ✅ Graceful error recovery
- ✅ User-friendly prompts

### 2. Extensibility
- ✅ Modular design, easy to extend
- ✅ Clear interface definitions
- ✅ Support custom analysis types
- ✅ Configurable scoring weights
- ✅ Plugin-style AI integration

### 3. Performance Optimization
- ✅ Batch operations reduce API calls
- ✅ Configurable result limits
- ✅ Progress indicators avoid user anxiety
- ✅ Reasonable timeout settings
- ✅ Incremental data collection

### 4. User Experience
- ✅ Beautiful terminal output
- ✅ Interactive and command modes
- ✅ Rich usage examples
- ✅ Detailed documentation and help
- ✅ Friendly error prompts

## License

MIT License - Copyright (c) 2025 GitHub PR Analyzer

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software.

---

**Built with ❤️ for the developer community**
