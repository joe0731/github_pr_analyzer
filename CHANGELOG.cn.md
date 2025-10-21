# Changelog

All notable changes to GitHub PR Analyzer will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2025-01-21

### 新增功能
- 🔍 **AI 智能搜索**：使用 cursor-agent 的智能关键词提取
  - 自动分析用户查询并提取最优搜索关键词
  - 按相关性和区分度对关键词排序
  - 支持 AI 不可用时的回退模式
- 📅 **增强的日期时间显示**：全面的日期时间信息
  - 搜索结果表格新增日期时间列
  - PR 和 commit 详情显示完整日期时间
  - 统一的 MM-DD HH:MM 格式便于快速查看
- ⚙️ **环境变量配置**：简化的设置方式
  - 移除对 .env 文件的依赖
  - 直接使用环境变量配置
  - 无需配置文件

### 功能变更
- 🔧 **搜索算法**：AI 驱动的关键词提取增强
  - 新增 `--smart-search` / `--no-smart-search` 选项
  - 默认启用智能搜索
  - 多关键词权重评分系统
- 📊 **显示格式**：改进的信息展示
  - 搜索结果现在显示创建/提交日期
  - PR 详情包含创建、更新和合并日期
  - Commit 详情显示创作和提交时间戳
- 🏗️ **配置系统**：简化的设置流程
  - 移除 python-dotenv 依赖
  - 直接使用 os.getenv() 获取环境变量

### 移除内容
- 📄 **配置文件**：不再需要
  - 移除 .env.example 文件
  - 移除 python-dotenv 依赖
  - 简化安装过程

### 技术改进
- 🧠 **智能搜索分析器**：AI 驱动搜索的新模块
- 🛠️ **工具函数**：增强的日期时间格式化工具
- 🎨 **界面增强**：带有日期时间信息的更好表格布局

## [1.0.0] - 2025-01-21

### Added
- Initial release of GitHub PR Analyzer
- PR collection from GitHub repositories using gh CLI
- Commit collection from Git repositories
- Support for merge commits detection and analysis
- Intelligent fuzzy search for PRs and commits
- Multiple search strategies (exact match, fuzzy match, multi-field search)
- Diff viewer with syntax highlighting
- AI-powered analysis using cursor-agent CLI
- Interactive command-line interface
- Rich terminal UI with tables, panels, and colors
- Batch analysis capabilities
- Report generation and export
- Configuration management via .env files
- Comprehensive error handling and validation
- Prerequisites checking system

### Features

#### Data Collection
- Collect all open PRs from repository
- Collect merged PRs within configurable time range
- Collect merge commits from Git history
- Auto-detect repository from Git remote
- Support for manual repository specification

#### Search and Matching
- Keyword-based search across PRs and commits
- Fuzzy matching with configurable threshold
- Multi-field search (title, body, author, labels)
- Scoring system (0-100) for match quality
- Configurable minimum score and result limits

#### Diff Viewing
- View PR diffs using gh CLI
- View commit diffs using GitPython
- Syntax-highlighted diff output
- File list display
- Support for file content comparison

#### AI Analysis
- Integration with cursor-agent CLI
- Automatic summarization of changes
- Impact analysis
- Technical analysis
- Batch analysis of multiple items
- Markdown report generation

#### User Interface
- Beautiful terminal output using Rich library
- Interactive mode with menu navigation
- Command-line interface with multiple subcommands
- Progress indicators for long operations
- Color-coded results and status messages
- Tabular display of search results

#### Commands
- `collect`: Collect PRs and commits from repository
- `search`: Search for matching PRs and commits
- `view-pr`: View specific PR details
- `view-commit`: View specific commit details
- `interactive`: Launch interactive mode

### Documentation
- Comprehensive README with features and quick start
- Detailed USAGE guide with examples and scenarios
- Step-by-step INSTALL guide for all platforms
- API documentation in docstrings
- Configuration examples

### Infrastructure
- MIT License for commercial and personal use
- Requirements file with pinned dependencies
- Setup.py for package distribution
- Environment variable configuration
- .gitignore for Python projects
- Installation test script

### Security
- Safe command execution with error handling
- No hardcoded credentials
- Environment-based configuration
- Input validation and sanitization

## [Unreleased]

### Planned Features
- Support for GitLab and Bitbucket
- Advanced filtering options (by label, author, date range)
- Export to JSON, CSV formats
- Web dashboard interface
- Plugin system for custom analyzers
- Caching mechanism for performance
- Multi-repository analysis
- Diff statistics and visualization
- Integration with CI/CD systems
- Custom report templates

### Known Issues
- Large diffs may be truncated in display
- AI analysis depends on external cursor-agent tool
- Network timeouts on slow connections
- Memory usage for very large repositories

---

[1.0.0]: https://github.com/yourusername/github-pr-analyzer/releases/tag/v1.0.0
