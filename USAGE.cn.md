# 使用指南

[中文文档](USAGE.cn.md) | English

## 命令详解

### `interactive` (交互模式)
启动菜单驱动的界面。推荐首次使用者使用。
```bash
gh-pr-analyzer interactive
```

### `search` (搜索)
搜索 PR 和 commits。
```bash
# 基本搜索
gh-pr-analyzer search "query"

# 带 AI 分析
gh-pr-analyzer search "query" --analyze

# 选项
--repo, -r      目标仓库 (默认: 当前仓库)
--months, -m    回溯月数 (默认: $DEFAULT_MONTHS 或 3)
--analyze, -a   启用 AI 分析
--show-diff, -d 显示代码变更
--smart-search  启用/禁用 AI 关键词提取
```

### `collect` (收集)
收集统计信息 (开放/已合并 PR, commits)。
```bash
gh-pr-analyzer collect --months 6
```

### `traverse` (遍历)
批量分析近期 PR，适用于生成报告。
```bash
gh-pr-analyzer traverse --days 7
```

### `view-pr` / `view-commit` (查看详情)
查看特定项目的详细信息。
```bash
gh-pr-analyzer view-pr 123 --analyze
gh-pr-analyzer view-commit <SHA>
```

## 配置说明

工具通过环境变量进行配置：

- **`CURSOR_AGENT_PATH`**: `cursor-agent` 可执行文件路径。使用 `--analyze` 和智能搜索时**必须配置**。
- **`DEFAULT_MONTHS`**: `collect` 和 `search` 命令的默认回溯月数 (默认: 3)。
- **`DEFAULT_REPO_PATH`**: 查找 git 仓库的默认路径 (默认: 当前目录)。
