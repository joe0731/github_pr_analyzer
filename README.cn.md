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
gh-pr-analyzer collect

# 4. 生成日报/周报
gh-pr-analyzer traverse --days 7
```

## ✨ 主要特性
- 🔍 **智能搜索**: AI 驱动的关键词提取
- 📊 **数据收集**: PR 和 merge commit 统计
- 🔄 **Diff 查看**: 语法高亮的代码变更展示
- 🤖 **AI 分析**: 集成 cursor-agent 自动总结
- 📅 **遍历模式**: 批量分析用于生成报告

详细命令用法请参阅 [USAGE.cn.md](USAGE.cn.md)。
