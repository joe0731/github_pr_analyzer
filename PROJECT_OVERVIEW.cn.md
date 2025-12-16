# GitHub PR & Commit Analyzer - 项目概览

[中文文档](PROJECT_OVERVIEW.cn.md) | English

## 项目简介

GitHub PR & Commit Analyzer 是一个商用级别的命令行工具，用于智能收集、分析和总结 GitHub Pull Requests 和提交记录。

**版本**: 3.0.4  
**PyPI**: `github-pr-analyzer`

## 技术架构

### 架构设计

```
┌─────────────────────────────────────────────────────────┐
│               CLI Interface (ghpa)                     │
│  - 命令解析 (Click)                                     │
│  - 用户交互 (Rich)                                      │
└──────────────┬──────────────────────────────────────────┘
               │
        ┌──────┴───────┐
        │              │
┌───────▼──────┐  ┌───▼──────────┐
│ PR Collector │  │Commit Collec.│
│ (gh CLI)     │  │ (GitPython)  │
└──────┬───────┘  └───┬──────────┘
       │              │
       └──────┬───────┘
              │
       ┌──────▼───────┐
       │   Matcher    │
       │ (模糊/AI)    │
       └──────┬───────┘
              │
    ┌─────────┴─────────┐
    │                   │
┌───▼─────────┐  ┌──────▼────────┐
│ Diff Viewer │  │  AI Analyzer  │
└─────────────┘  └───────────────┘
```

### 模块说明

- **src/cli.py**: 入口点 (`ghpa`，兼容旧命令 `gh-pr-analyzer`)，处理命令 (`search`, `collect`, `traverse` 等)。
- **src/pr_collector.py**: 封装 GitHub CLI (`gh`) 获取 PR 数据。
- **src/commit_collector.py**: 使用 GitPython 检查本地 git 历史。
- **src/matcher.py**: 实现模糊搜索和 AI 关键词提取。
- **src/ai_analyzer.py**: 集成外部 `cursor-agent` 进行 LLM 分析。
- **src/diff_viewer.py**: 渲染语法高亮的 diff。

## 依赖项

- **Python 3.8+**
- **Git** & **GitHub CLI (gh)**
- **Python 包**: `click`, `rich`, `requests`, `gitpython`, `fuzzywuzzy`, `python-levenshtein`, `python-dateutil`
