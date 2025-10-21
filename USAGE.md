# Usage Guide

[中文文档](USAGE.cn.md) | English

This document provides detailed usage instructions and best practices.

## Quick Start

### 1. Installation and Configuration

```bash
# Navigate to project directory
cd github-pr-analyzer

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
# or venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env
# Edit .env file, configure cursor-agent path (optional)
```

### 2. Verify Installation

```bash
# Check prerequisites
python main.py collect --help

# Should see command help information
```

## Command Details

### collect - Collect Data

Collect all PR and commit data from specified repository.

```bash
# Basic usage (auto-detect current repository)
python main.py collect

# Specify repository
python main.py collect --repo nvidia/TensorRT-Model-Optimizer

# Custom time range
python main.py collect --months 6

# Complete example
python main.py collect --repo owner/repo --months 3
```

**Example Output:**
```
✓ Found 45 open PRs
✓ Found 123 merged PRs
✓ Found 89 merge commits
```

### search - Smart Search

Search for relevant PRs and commits based on keywords.

```bash
# Basic search
python main.py search "fix memory leak"

# Search with parameters
python main.py search "add feature" \
  --repo owner/repo \
  --months 3 \
  --min-score 40 \
  --max-results 15

# Search and show diff
python main.py search "optimization" --show-diff

# Search and perform AI analysis
python main.py search "refactor database" --analyze

# Full features (search + diff + AI analysis)
python main.py search "authentication" \
  --analyze \
  --show-diff \
  --max-results 5
```

**Parameter Descriptions:**
- `--repo, -r`: Specify repository (format: owner/repo)
- `--months, -m`: Search range (months), default 3
- `--min-score`: Minimum match score (0-100), default 30
- `--max-results`: Maximum number of results, default 20
- `--analyze, -a`: Enable AI analysis
- `--show-diff, -d`: Show code changes

### view-pr - View PR Details

View complete information about a specific PR.

```bash
# Basic usage
python main.py view-pr 123

# Specify repository
python main.py view-pr 123 --repo owner/repo

# View and perform AI analysis
python main.py view-pr 123 --analyze
```

### view-commit - View Commit Details

View complete information about a specific commit.

```bash
# Use full SHA
python main.py view-commit abc123def456

# Use short SHA
python main.py view-commit abc123

# With AI analysis
python main.py view-commit abc123 --analyze
```

### interactive - Interactive Mode

Launch interactive interface with menu-driven operations.

```bash
python main.py interactive
```

**Interactive Mode Features:**
1. Search query
2. View specific PR
3. View specific commit
4. Exit

## Use Case Examples

### Scenario 1: Discover All Security-Related Changes

```bash
# Search for security-related PRs and commits
python main.py search "security vulnerability fix CVE" \
  --months 6 \
  --min-score 50 \
  --analyze

# View generated analysis report
# Report includes:
# - All security-related changes
# - Detailed analysis of each change
# - Impact scope and risk assessment
```

### Scenario 2: Prepare Release Notes

```bash
# Collect recent merge commits
python main.py collect --months 1

# Search for feature-related changes
python main.py search "feature" --analyze --max-results 30

# Search for bug fix-related changes
python main.py search "fix bug" --analyze --max-results 30

# Generated reports can be used as basis for release notes
```

### Scenario 3: Code Review Preparation

```bash
# View complete information about specific PR
python main.py view-pr 456 --analyze

# Output includes:
# - PR description and statistics
# - Complete code diff (with highlighting)
# - AI-generated technical analysis
# - Potential impact and risk assessment
```

## AI Analysis Features

### Configure cursor-agent

1. Ensure cursor-agent CLI is installed
2. Set path in `.env` file:
   ```
   CURSOR_AGENT_PATH=/usr/local/bin/cursor-agent
   ```

### Analysis Types

Tool supports three analysis types (extensible in code):

1. **summary**: Quickly understand purpose and impact of change
2. **impact**: Assess impact scope and risks of change
3. **technical**: In-depth technical implementation details

### Analysis Output

AI analysis generates:
- Markdown-formatted analysis reports
- Structured information (purpose, impact, technical details, etc.)
- Optional save to file functionality

### Batch Analysis

```bash
# Search and analyze top 10 matches
python main.py search "optimization" --analyze --max-results 10

# System will:
# 1. Search for matching PR/commits
# 2. Fetch diff for each
# 3. Call AI for analysis
# 4. Display all analysis results
# 5. Ask whether to save report
```

## Best Practices

### 1. Regular Data Collection

Recommended to regularly run collect command to understand repository status:
```bash
python main.py collect --months 3
```

### 2. Use Descriptive Search Terms

Good search term examples:
- ✅ "authentication security token"
- ✅ "database migration schema"
- ✅ "API endpoint REST"

Poor search terms:
- ❌ "fix" (too broad)
- ❌ "update" (too vague)
- ❌ "a" (single character)

### 3. Use AI Analysis Wisely

AI analysis consumes resources, recommendations:
- Search first, filter most relevant results
- Only use AI analysis for important PRs/commits
- Use --max-results to limit analysis quantity

### 4. Save Analysis Reports

For important analyses, choose to save reports:
```bash
python main.py search "critical security" --analyze
# When prompted, select "Yes" to save report
```

Report file naming format: `pr_analysis_report_owner_repo.md`

## Troubleshooting

### Problem: command not found: gh

**Solution:**
```bash
# Install GitHub CLI
# Ubuntu/Debian:
sudo apt install gh

# macOS:
brew install gh

# Then login
gh auth login
```

### Problem: cannot detect repository

**Solution:**
```bash
# Make sure you're in Git repository directory
git remote -v

# Or explicitly specify repository
python main.py collect --repo owner/repo
```

### Problem: AI analysis not available

**Reason:** cursor-agent not configured

**Solution:**
1. Check if cursor-agent is installed
2. Configure correct path in `.env`
3. Test if cursor-agent is available

## Performance Optimization

### 1. Large Repositories

For repositories with many PRs:
```bash
# Limit time range
python main.py collect --months 1

# Limit search results
python main.py search "query" --max-results 10
```

### 2. Network Issues

If network is slow:
- GitHub CLI will automatically handle retries
- Consider reducing months parameter
- Collect data in batches

---

For more information, see [README.md](README.md)

## License

MIT License - Copyright (c) 2025 GitHub PR Analyzer
