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
--save-json     Save matched PRs as JSON datasets
--output-dir    Directory for JSON files (default: pr_exports)
```

### `collect`
Collect statistics (open/merged PRs, commits).
```bash
gh-pr-analyzer collect --months 6 --save-json --output-dir ./exports
```

### `traverse`
Batch analyze recent PRs for reports.
```bash
gh-pr-analyzer traverse --days 7 --save-json
```

### `view-pr` / `view-commit`
View details of a specific item.
```bash
gh-pr-analyzer view-pr 123 --analyze --output-dir ./exports   # JSON export enabled by default
gh-pr-analyzer view-commit <SHA>
```

### JSON Export Notes
- `view-pr` writes a JSON file automatically unless `--no-save-json` is supplied.
- `collect`, `search`, and `traverse` export the PRs they touch when `--save-json` is present.
- Files are saved under `pr_exports/` by default with the suffix `repo_name_<pr>_<title>.json` and contain PR metadata, every commit (ID, title, message, per-file diff), plus the full review conversation. See [README](README.md#-json-export-format) for a schema overview.

## Configuration

The tool is configured via environment variables:

- **`CURSOR_AGENT_PATH`**: Path to `cursor-agent` executable. **Required** for `--analyze` and Smart Search.
- **`DEFAULT_MONTHS`**: Default months to look back in `collect` and `search` (Default: 3).
- **`DEFAULT_REPO_PATH`**: Default path to look for git repo (Default: current dir).
