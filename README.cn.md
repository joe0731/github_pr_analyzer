# GitHub PR & Commit Analyzer

[English](README.md) | 中文文档

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

# 2. AI 智能搜索 (英文输出)
gh-pr-analyzer search "authentication bug" --analyze

# 3. AI 智能搜索 (中文输出)
gh-pr-analyzer search "authentication bug" --analyze -cn

# 4. 收集数据
gh-pr-analyzer collect --save-json

# 5. 生成日报/周报并导出
gh-pr-analyzer traverse --days 7 --save-json
gh-pr-analyzer traverse -r pytorch/pytorch --days 7 --save-json -cn
```

所有命令都提供成对的 `--save-json` / `--no-save-json` 开关，需要导出时随时打开，不想生成则显式关闭（例如 `view-pr` 默认导出，配合 `--no-save-json` 可跳过写入）。

### 语言选项

使用 `-cn` 或 `--chinese` 参数可获得中文 AI 分析输出：

```bash
# 中文输出
gh-pr-analyzer search "quantization" -a -cn
gh-pr-analyzer view-pr 588 -a -cn
gh-pr-analyzer traverse --days 7 -cn
```

## ✨ 主要特性
- 🔍 **智能搜索**: AI 驱动的关键词提取
- 📊 **数据收集**: PR 和 merge commit 统计
- 🔄 **Diff 查看**: 语法高亮的代码变更展示
- 🤖 **AI 分析**: 集成 cursor-agent 自动总结，支持中英文输出
- 📅 **遍历模式**: 批量分析用于生成报告
- 🗂 **JSON 导出**: 将 PR、commit 与完整对话保存为结构化 JSON
- 🌐 **多语言支持**: AI 分析支持中英文输出
- 💾 **即时保存**: 每个 PR 分析完成后立即保存 JSON 文件
- 🎨 **美化显示**: 终端输出带有颜色和格式美化

详细命令用法请参阅 [USAGE.cn.md](USAGE.cn.md)。

## 🗂 JSON 导出格式

`collect`、`search`、`traverse`、`view-pr` 共享同一组 `--save-json` / `--no-save-json` 选项（其中 `view-pr` 默认开启，可用 `--no-save-json` 关闭）。文件默认写入 `gh_pr_exports/`，也可通过 `--output-dir` 自定义目录。

### 文件命名规则

文件命名格式：
```
{仓库名}_{merged_pr|open_pr}_{PR编号}_{标题}_{时间戳}.json
```

示例：
- `NVIDIA_TensorRT_merged_pr_588_Support_AutoQuantize_20251125_1423.json`
- `pytorch_pytorch_open_pr_123_Add_feature_20251126_0930.json`

时间戳：已合入 PR 使用合入时间，未合入 PR 使用最后更新时间。

### JSON 结构

每个 JSON 文件包含：

- `repo`: 形如 `owner/repo` 的仓库标识
- `pr`: PR 基本信息，包含：
  - `number`, `title`, `url`, `state`
  - `author`, `author_name`, `author_email`
  - `created_at`, `updated_at`, `merged_at`
  - `base_ref`, `head_ref`
  - `body`: PR 描述（行数组格式，便于阅读）
- `commits`: PR 关联提交列表，包含：
  - `id`: 完整 commit SHA
  - `title`: commit 第一行标题
  - `message`: 完整 commit message
  - `committer_name`, `committer_email`
  - `files`: `{ "path": "<文件路径>", "diff": ["行1", "行2", ...] }` 数组
- `conversation`: 审查会话数据
  - `issue_comments`: PR 页面上的讨论
  - `review_threads`: 代码审查线程（注：GitHub API 支持有限）
  - `reviews`: 审查结论（approve / comment / request changes）

> 示例片段：
```json
{
  "repo": "octo-org/octo-repo",
  "pr": {
    "number": 42,
    "title": "Fix login",
    "author": "octocat",
    "author_name": "The Octocat",
    "author_email": "octocat@github.com",
    "state": "MERGED",
    "body": [
      "## 摘要",
      "此 PR 修复了登录流程。",
      "",
      "## 变更内容",
      "- 修复身份验证"
    ]
  },
  "commits": [
    {
      "id": "abc123...",
      "title": "Adjust auth flow",
      "message": "Adjust auth flow\n\n- add checks...\n",
      "committer_name": "The Octocat",
      "committer_email": "octocat@github.com",
      "files": [
        {
          "path": "auth/login.py",
          "diff": [
            "@@ -1,3 +1,4 @@",
            " import os",
            "-old_line",
            "+new_line"
          ]
        }
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

## 🎨 AI 分析显示

AI 分析输出特性：
- **元数据面板**: 显示作者、邮箱、状态、URL，状态带颜色标识
- **分析面板**: 深色背景配白色文字，提升可读性
- **左对齐内容**: 所有文本左对齐，阅读体验更佳
- **自适应宽度**: 自动适配终端窗口大小

状态指示：
- ✅ **MERGED** 已合入（紫色）
- 🔄 **OPEN** 开放中（绿色）
- ❌ **CLOSED** 已关闭（红色）
