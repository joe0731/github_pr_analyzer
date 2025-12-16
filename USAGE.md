# Usage Guide

[中文文档](USAGE.cn.md) | English

## Commands

### `check`
Verify environment configuration and GitHub API connectivity.

```bash
# basic
ghpa check

# verify repo access
ghpa check -r owner/repo

# raw JSON for automation
ghpa check --json
```

### `interactive`
Launch the menu-driven interface. Best for first-time users.
```bash
ghpa interactive
```

### `search`
Search for PRs and commits.
```bash
# Basic
ghpa search "query"

# With AI analysis
ghpa search "query" --ai

# Options
--repo, -r      Target repository (default: current)
--months, -m    Months to look back (default: $DEFAULT_MONTHS or 3)
--ai            Enable AI analysis (requires CURSOR_AGENT_PATH)
--show-diff, -d Show code changes
--smart-search  Enable/disable AI keyword extraction (requires --ai)
--save-json     Save matched PRs as JSON datasets
--output-dir    Directory for JSON files (default: gh_pr_exports)
```

### `collect`
Collect statistics (open/merged PRs, commits).
```bash
ghpa collect --months 6 --save-json --output-dir ./exports
```

### `traverse`
Batch analyze recent PRs for reports.
```bash
ghpa traverse --days 7 --save-json
```

### `view-pr` / `view-commit`
View details of a specific item.
```bash
ghpa view-pr 123 --ai --output-dir ./exports   # JSON export enabled by default
ghpa view-commit <SHA>
```

### JSON Export Notes
- `view-pr` writes a JSON file automatically unless `--no-save-json` is supplied.
- `collect`, `search`, and `traverse` export the PRs they touch when `--save-json` is present.
- Files are saved under `gh_pr_exports/` by default with the suffix `repo_name_<pr>_<title>.json` and contain PR metadata, every commit (ID, title, message, per-file diff), plus the full review conversation. See [README](README.md#-json-export-format) for a schema overview.

## Configuration

The tool is configured via environment variables:

- **`CURSOR_AGENT_PATH`**: Path to `cursor-agent` executable. Required for `--ai` and Smart Search.
- **`DEFAULT_MONTHS`**: Default months to look back in `collect` and `search` (Default: 3).
- **`DEFAULT_REPO_PATH`**: Default path to look for git repo (Default: current dir).
