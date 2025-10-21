# Changelog

[中文文档](CHANGELOG.cn.md) | English

All notable changes to GitHub PR Analyzer will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
- Bilingual documentation (English and Chinese)

### Infrastructure
- MIT License for commercial and personal use
- Requirements file with pinned dependencies
- Setup.py for package distribution
- Environment variable configuration
- .gitignore for Python projects
- Installation test script
- License headers in all Python files

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

## License

MIT License - Copyright (c) 2025 GitHub PR Analyzer
