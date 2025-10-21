# Installation Guide

[中文文档](INSTALL.cn.md) | English

This document provides detailed installation steps and dependency configuration instructions.

## System Requirements

- **Operating System**: Linux, macOS, Windows
- **Python**: 3.8 or higher
- **Disk Space**: At least 100MB
- **Network**: Access to GitHub API required

## Dependency Checklist

Before starting installation, please confirm the following dependencies:

- [ ] Python 3.8+
- [ ] Git
- [ ] GitHub CLI (gh)
- [ ] cursor-agent (optional, for AI features)

## Detailed Installation Steps

### Step 1: Install Python

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
python3 --version  # verify version >= 3.8
```

#### macOS
```bash
# Using Homebrew
brew install python@3.11

# Or download from: https://www.python.org/downloads/
python3 --version
```

#### Windows
1. Download installer from [python.org](https://www.python.org/downloads/)
2. Run installer, check "Add Python to PATH"
3. Verify installation:
```cmd
python --version
```

### Step 2: Install Git

#### Linux (Ubuntu/Debian)
```bash
sudo apt install git
git --version
```

#### macOS
```bash
# Usually pre-installed, or use Homebrew
brew install git
```

#### Windows
Download and install from [git-scm.com](https://git-scm.com/download/win)

### Step 3: Install GitHub CLI

GitHub CLI is a core dependency of this tool.

#### Linux (Ubuntu/Debian)
```bash
# Method 1: Using official PPA
type -p curl >/dev/null || sudo apt install curl -y
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
sudo chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
sudo apt update
sudo apt install gh

# Method 2: Using package manager
sudo apt install gh  # Debian/Ubuntu 22.04+
```

#### macOS
```bash
brew install gh
```

#### Windows
```powershell
# Using Chocolatey
choco install gh

# Or using Scoop
scoop install gh

# Or download installer from https://github.com/cli/cli/releases
```

#### Verify Installation
```bash
gh --version
```

#### Login to GitHub
```bash
gh auth login

# Follow prompts to choose:
# 1. GitHub.com
# 2. HTTPS
# 3. Login with a web browser (recommended)
# Or Paste an authentication token
```

Verify login status:
```bash
gh auth status
```

### Step 4: Install This Tool

#### Method A: Install from Source (Recommended)

```bash
# 1. Clone or download project
cd /path/to/github-pr-analyzer

# 2. Create virtual environment
python3 -m venv venv

# 3. Activate virtual environment
# Linux/macOS:
source venv/bin/activate

# Windows:
venv\Scripts\activate

# 4. Upgrade pip
pip install --upgrade pip

# 5. Install dependencies
pip install -r requirements.txt

# 6. Verify installation
python main.py --help
```

#### Method B: Install Using setup.py

```bash
# In project directory
pip install -e .

# After installation, you can use the command directly
gh-pr-analyzer --help
```

### Step 5: Configure Environment Variables

```bash
# 1. Copy configuration template
cp .env.example .env

# 2. Edit configuration file
nano .env  # or use another editor

# 3. Example configuration
CURSOR_AGENT_PATH=/usr/local/bin/cursor-agent  # optional
DEFAULT_MONTHS=3
DEFAULT_REPO_PATH=.
```

### Step 6: Install cursor-agent (Optional)

If you need AI analysis features:

```bash
# Specific installation method depends on cursor-agent's release method
# Please refer to cursor-agent's official documentation

# After installation, configure path in .env
CURSOR_AGENT_PATH=/path/to/cursor-agent
```

## Dependency Packages

This tool uses the following Python packages:

### Core Dependencies
- **click** (>= 8.1.0): CLI framework
- **rich** (>= 13.0.0): Terminal beautification
- **GitPython** (>= 3.1.40): Git repository operations
- **requests** (>= 2.31.0): HTTP requests
- **python-dotenv** (>= 1.0.0): Environment variable management

### Search and Matching
- **fuzzywuzzy** (>= 0.18.0): Fuzzy string matching
- **python-levenshtein** (>= 0.21.0): String distance calculation

### Utilities
- **python-dateutil** (>= 2.8.2): Date processing

## Verify Installation

Run the following commands to verify all components:

```bash
# 1. Check Python
python --version

# 2. Check Git
git --version

# 3. Check GitHub CLI
gh --version
gh auth status

# 4. Check tool itself
python main.py --help

# 5. Run prerequisites check
python test_installation.py
```

Expected output:
```
Checking prerequisites...
✓ Git found
✓ GitHub CLI found and authenticated
✓ All prerequisites met
```

## Common Installation Issues

### Issue 1: pip install fails

**Symptoms:**
```
ERROR: Could not find a version that satisfies the requirement...
```

**Solution:**
```bash
# Upgrade pip
pip install --upgrade pip

# Use mirror (if in China)
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### Issue 2: GitPython installation fails

**Solution:**
```bash
# Linux: Install development tools
sudo apt install python3-dev build-essential

# macOS: Install Xcode Command Line Tools
xcode-select --install

# Then reinstall
pip install gitpython
```

### Issue 3: gh auth login fails

**Solution:**
```bash
# 1. Check network connection
curl https://github.com

# 2. Use token login
gh auth login --with-token < token.txt

# 3. Or use SSH
gh auth login --git-protocol ssh
```

## Uninstallation

If you need to uninstall the tool:

```bash
# 1. Deactivate virtual environment
deactivate

# 2. Remove virtual environment
rm -rf venv

# 3. Remove project directory
cd ..
rm -rf github-pr-analyzer
```

## Update

Update to the latest version:

```bash
# 1. Activate virtual environment
source venv/bin/activate

# 2. Pull latest code (if using git)
git pull

# 3. Update dependencies
pip install --upgrade -r requirements.txt

# 4. Verify
python main.py --version
```

---

After installation is complete, please see [USAGE.md](USAGE.md) for usage instructions.

## License

MIT License - Copyright (c) 2025 GitHub PR Analyzer
