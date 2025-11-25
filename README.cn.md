# GitHub PR & Commit Analyzer

[中文文档](README.cn.md) | English

一个强大的命令行工具，用于智能收集、分析和总结 GitHub Pull Requests 和提交记录。

[![PyPI version](https://badge.fury.io/py/github-pr-analyzer.svg)](https://badge.fury.io/py/github-pr-analyzer)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🚀 安装与设置

### 1. 前置要求
- **Python 3.8+**
- **Git**
- **GitHub CLI (gh)**: 必须完成登录 (`gh auth login`)

### 2. 安装
```bash
pip install github-pr-analyzer
```

### 3. 配置 (环境变量)

| 变量名 | 描述 | 默认值 | 是否必须 |
|--------|------|--------|----------|
| `CURSOR_AGENT_PATH` | cursor-agent 路径 (用于 AI 功能) | 无 | **是** (使用 AI 时) |
| `DEFAULT_MONTHS` | 数据回溯的月数 | `3` | 否 |
| `DEFAULT_REPO_PATH` | 默认仓库路径 | `.` | 否 |

```bash
# 配置示例
export CURSOR_AGENT_PATH=/path/to/cursor-agent
export DEFAULT_MONTHS=6
```

## 📖 快速开始

```bash
# 1. 交互模式 (推荐新手使用)
gh-pr-analyzer interactive

# 2. AI 智能搜索
gh-pr-analyzer search "authentication bug" --analyze

# 3. 收集数据
gh-pr-analyzer collect --save-json

# 4. 生成日报/周报并导出
gh-pr-analyzer traverse --days 7 --save-json
gh-pr-analyzer traverse -r pytorch/pytorch --days 7 --save-json

```

## ✨ 主要特性
- 🔍 **智能搜索**: AI 驱动的关键词提取
- 📊 **数据收集**: PR 和 merge commit 统计
- 🔄 **Diff 查看**: 语法高亮的代码变更展示
- 🤖 **AI 分析**: 集成 cursor-agent 自动总结
- 📅 **遍历模式**: 批量分析用于生成报告
- 🗂 **JSON 导出**: 将 PR、commit 与完整对话保存为结构化 JSON

详细命令用法请参阅 [USAGE.cn.md](USAGE.cn.md)。

## 🗂 JSON 导出格式

`collect`、`search`、`traverse`、`view-pr` 均支持通过 `--save-json` 输出结构化数据（`view-pr` 默认开启）。文件默认写入 `pr_exports/`，也可通过 `--output-dir` 自定义目录，命名规则为 `repo_name_<pr_num>_<pr_title>.json`。

每个 JSON 文件包含：

- `repo`: 形如 `owner/repo` 的仓库标识
- `pr`: PR 基本信息（编号、标题、作者、状态、描述、base/head 分支、时间戳、URL）
- `commits`: PR 关联提交列表，包含
  - `id`: 完整 commit SHA
  - `title`: commit 第一行标题
  - `message`: 完整 commit message
  - `files`: `{ "path": "<文件路径>", "diff": "<统一 diff 内容>" }` 数组
- `conversation`: 审查会话数据
  - `issue_comments`: PR 页面上的讨论
  - `review_threads`: 代码审查线程，含每条评论、状态、是否已解决
  - `reviews`: 审查结论（approve / comment / request changes）

> 示例片段：
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

借助该格式可轻松串接自定义分析、审计或归档流程。
