# GitHub PR Analyzer - Quick Start Guide

[中文文档](QUICK_START_GUIDE.cn.md) | English

## 5-Minute Quick Start

### Step 1: Run Auto-Installation Script

```bash
# Navigate to project directory
cd github-pr-analyzer

# Run quick start script
./quick_start.sh
```

The script will automatically:
- ✅ Check Python, Git, gh CLI
- ✅ Verify gh CLI authentication
- ✅ Create virtual environment
- ✅ Install all dependencies
- ✅ Create configuration file

### Step 2: Run Installation Test

```bash
python test_installation.py
```

If you see "All tests passed!", the installation is successful!

### Step 3: First Use

#### Try Interactive Mode (Recommended for Beginners)

```bash
python main.py interactive
```

Interactive mode will guide you through all operations.

#### Or Use Command-Line Mode

```bash
# Search in current Git repository
python main.py search "bug fix"

# View specific PR
python main.py view-pr 123
```

## Common Commands Cheat Sheet

### Collect Data
```bash
# Collect PRs and commits from current repository (last 3 months)
python main.py collect

# Collect from specified repository (6 months)
python main.py collect --repo owner/repo --months 6
```

### Search
```bash
# Basic search
python main.py search "authentication"

# With AI analysis
python main.py search "security fix" --analyze

# Show code changes
python main.py search "refactor" --show-diff

# Full features
python main.py search "feature" \
  --analyze \
  --show-diff \
  --max-results 5
```

### View Details
```bash
# View PR
python main.py view-pr 123 --analyze

# View commit
python main.py view-commit abc1234 --analyze
```

## Configure AI Analysis (Optional)

If you want to use AI analysis features:

1. Install cursor-agent CLI
2. Edit `.env` file:
```bash
CURSOR_AGENT_PATH=/path/to/cursor-agent
```

3. Add `--analyze` parameter when searching or viewing

## Get Help

```bash
# View all commands
python main.py --help

# View help for specific command
python main.py search --help
python main.py collect --help
```

## Next Steps

- 📖 Read [README.md](README.md) to learn about all features
- 📚 Check [USAGE.md](USAGE.md) for detailed usage
- 🔧 Refer to [INSTALL.md](INSTALL.md) for installation troubleshooting
- 🏗️ Read [PROJECT_OVERVIEW.md](PROJECT_OVERVIEW.md) for architecture

## Common Issues

**Q: Getting "gh not authenticated"**  
A: Run `gh auth login` to login to GitHub

**Q: Repository not found**  
A: Make sure you're in a Git repository directory, or use `--repo` to specify

**Q: No search results**  
A: Try lowering the `--min-score` parameter

---

**Happy analyzing!** 🎉

For issues, please check documentation or submit an Issue.
