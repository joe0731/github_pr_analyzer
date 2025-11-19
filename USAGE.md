# Usage Guide

[中文文档](USAGE.cn.md) | English

## Commands

### `interactive`
Launch the menu-driven interface. Best for first-time users.
```bash
gh-pr-analyzer interactive
```

### `search`
Search for PRs and commits.
```bash
# Basic
gh-pr-analyzer search "query"

# With AI analysis
gh-pr-analyzer search "query" --analyze

# Options
--repo, -r      Target repository (default: current)
--months, -m    Months to look back (default: $DEFAULT_MONTHS or 3)
--analyze, -a   Enable AI analysis
--show-diff, -d Show code changes
--smart-search  Enable/disable AI keyword extraction
```

### `collect`
Collect statistics (open/merged PRs, commits).
```bash
gh-pr-analyzer collect --months 6
```

### `traverse`
Batch analyze recent PRs for reports.
```bash
gh-pr-analyzer traverse --days 7
```

### `view-pr` / `view-commit`
View details of a specific item.
```bash
gh-pr-analyzer view-pr 123 --analyze
gh-pr-analyzer view-commit <SHA>
```

## Configuration

The tool is configured via environment variables:

- **`CURSOR_AGENT_PATH`**: Path to `cursor-agent` executable. **Required** for `--analyze` and Smart Search.
- **`DEFAULT_MONTHS`**: Default months to look back in `collect` and `search` (Default: 3).
- **`DEFAULT_REPO_PATH`**: Default path to look for git repo (Default: current dir).
