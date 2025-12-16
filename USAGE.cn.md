# 使用指南

[中文文档](USAGE.cn.md) | English

## 命令详解

### `check` (连通性检查)
验证环境变量配置和 GitHub API 连通性。

```bash
# 基础检查
ghpa check

# 检查某个 repo 的访问权限
ghpa check -r owner/repo

# 输出 JSON（便于自动化）
ghpa check --json
```

### `interactive` (交互模式)
启动菜单驱动的界面。推荐首次使用者使用。
```bash
ghpa interactive
```

### `search` (搜索)
搜索 PR 和 commits。
```bash
# 基本搜索
ghpa search "query"

# 带 AI 分析
ghpa search "query" --ai

# 选项
--repo, -r      目标仓库 (默认: 当前仓库)
--months, -m    回溯月数 (默认: $DEFAULT_MONTHS 或 3)
--ai            启用 AI 分析（需要 CURSOR_AGENT_PATH）
--show-diff, -d 显示代码变更
--smart-search  启用/禁用 AI 关键词提取（需要 --ai）
--save-json     将匹配到的 PR 导出为 JSON
--output-dir    JSON 文件输出目录 (默认: gh_pr_exports)
```

### `collect` (收集)
收集统计信息 (开放/已合并 PR, commits)。
```bash
ghpa collect --months 6 --save-json --output-dir ./exports
```

### `traverse` (遍历)
批量分析近期 PR，适用于生成报告。
```bash
ghpa traverse --days 7 --save-json
```

### `view-pr` / `view-commit` (查看详情)
查看特定项目的详细信息。
```bash
ghpa view-pr 123 --ai --output-dir ./exports   # 默认开启 JSON 导出
ghpa view-commit <SHA>
```

### JSON 导出提示
- `view-pr` 默认写入 JSON，可通过 `--no-save-json` 关闭。
- `collect`、`search`、`traverse` 在传入 `--save-json` 时会导出所涉及的 PR。
- 文件默认位于 `gh_pr_exports/`，命名为 `repo_name_<pr>_<title>.json`，内容包括 PR 元信息、所有 commit（ID、标题、message、逐文件 diff）以及完整会话。结构说明见 [README.cn.md](README.cn.md#-json-导出格式)。

## 配置说明

工具通过环境变量进行配置：

- **`CURSOR_AGENT_PATH`**: `cursor-agent` 可执行文件路径。使用 `--ai` 和智能搜索时需要配置。
- **`DEFAULT_MONTHS`**: `collect` 和 `search` 命令的默认回溯月数 (默认: 3)。
- **`DEFAULT_REPO_PATH`**: 查找 git 仓库的默认路径 (默认: 当前目录)。
