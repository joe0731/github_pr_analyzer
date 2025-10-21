# 安装指南

本文档提供详细的安装步骤和依赖配置说明。

## 系统要求

- **操作系统**: Linux, macOS, Windows
- **Python**: 3.8 或更高版本
- **磁盘空间**: 至少 100MB
- **网络**: 需要访问 GitHub API

## 依赖检查清单

在开始安装前，请确认以下依赖：

- [ ] Python 3.8+
- [ ] Git
- [ ] GitHub CLI (gh)
- [ ] cursor-agent (可选，用于 AI 功能)

## 详细安装步骤

### 步骤 1: 安装 Python

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
python3 --version  # 验证版本 >= 3.8
```

#### macOS
```bash
# 使用 Homebrew
brew install python@3.11

# 或从官网下载: https://www.python.org/downloads/
python3 --version
```

#### Windows
1. 从 [python.org](https://www.python.org/downloads/) 下载安装器
2. 运行安装器，勾选 "Add Python to PATH"
3. 验证安装：
```cmd
python --version
```

### 步骤 2: 安装 Git

#### Linux (Ubuntu/Debian)
```bash
sudo apt install git
git --version
```

#### macOS
```bash
# 通常已预装，或使用 Homebrew
brew install git
```

#### Windows
从 [git-scm.com](https://git-scm.com/download/win) 下载并安装

### 步骤 3: 安装 GitHub CLI

GitHub CLI 是本工具的核心依赖。

#### Linux (Ubuntu/Debian)
```bash
# 方法 1: 使用官方 PPA
type -p curl >/dev/null || sudo apt install curl -y
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
sudo chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
sudo apt update
sudo apt install gh

# 方法 2: 使用包管理器
sudo apt install gh  # Debian/Ubuntu 22.04+
```

#### macOS
```bash
brew install gh
```

#### Windows
```powershell
# 使用 Chocolatey
choco install gh

# 或使用 Scoop
scoop install gh

# 或从 https://github.com/cli/cli/releases 下载安装器
```

#### 验证安装
```bash
gh --version
```

#### 登录 GitHub
```bash
gh auth login

# 按照提示选择：
# 1. GitHub.com
# 2. HTTPS
# 3. Login with a web browser (推荐)
# 或 Paste an authentication token
```

验证登录状态：
```bash
gh auth status
```

### 步骤 4: 安装本工具

#### 方法 A: 从源码安装（推荐）

```bash
# 1. 克隆或下载项目
cd /path/to/github-pr-analyzer

# 2. 创建虚拟环境
python3 -m venv venv

# 3. 激活虚拟环境
# Linux/macOS:
source venv/bin/activate

# Windows:
venv\Scripts\activate

# 4. 升级 pip
pip install --upgrade pip

# 5. 安装依赖
pip install -r requirements.txt

# 6. 验证安装
python main.py --help
```

#### 方法 B: 使用 setup.py 安装

```bash
# 在项目目录中
pip install -e .

# 安装后可以直接使用命令
gh-pr-analyzer --help
```

### 步骤 5: 配置环境变量

```bash
# 1. 复制配置模板
cp .env.example .env

# 2. 编辑配置文件
nano .env  # 或使用其他编辑器

# 3. 配置内容示例
CURSOR_AGENT_PATH=/usr/local/bin/cursor-agent  # 可选
DEFAULT_MONTHS=3
DEFAULT_REPO_PATH=.
```

### 步骤 6: 安装 cursor-agent (可选)

如果需要使用 AI 分析功能：

```bash
# 具体安装方法取决于 cursor-agent 的发布方式
# 请参考 cursor-agent 的官方文档

# 安装后，在 .env 中配置路径
CURSOR_AGENT_PATH=/path/to/cursor-agent
```

## 依赖包说明

本工具使用以下 Python 包：

### 核心依赖
- **click** (>= 8.1.0): 命令行界面框架
- **rich** (>= 13.0.0): 美化终端输出
- **GitPython** (>= 3.1.40): Git 仓库操作
- **requests** (>= 2.31.0): HTTP 请求
- **python-dotenv** (>= 1.0.0): 环境变量管理

### 搜索和匹配
- **fuzzywuzzy** (>= 0.18.0): 模糊字符串匹配
- **python-levenshtein** (>= 0.21.0): 字符串距离计算

### 工具包
- **python-dateutil** (>= 2.8.2): 日期处理

### 开发依赖（可选）
- **black** (>= 23.0.0): 代码格式化
- **flake8** (>= 6.0.0): 代码检查
- **mypy** (>= 1.0.0): 类型检查

## 验证安装

运行以下命令验证所有组件：

```bash
# 1. 检查 Python
python --version

# 2. 检查 Git
git --version

# 3. 检查 GitHub CLI
gh --version
gh auth status

# 4. 检查工具本身
python main.py --help

# 5. 运行前置条件检查
python -c "from src.cli import check_prerequisites; check_prerequisites()"
```

预期输出：
```
Checking prerequisites...
✓ Git found
✓ GitHub CLI found and authenticated
✓ All prerequisites met
```

## 常见安装问题

### 问题 1: pip install 失败

**症状:**
```
ERROR: Could not find a version that satisfies the requirement...
```

**解决方案:**
```bash
# 升级 pip
pip install --upgrade pip

# 使用国内镜像（如果在中国）
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### 问题 2: GitPython 安装失败

**症状:**
```
ERROR: Failed building wheel for gitpython
```

**解决方案:**
```bash
# Linux: 安装开发工具
sudo apt install python3-dev build-essential

# macOS: 安装 Xcode Command Line Tools
xcode-select --install

# 然后重新安装
pip install gitpython
```

### 问题 3: python-levenshtein 安装失败

**症状:**
```
ERROR: Failed building wheel for python-levenshtein
```

**解决方案:**
```bash
# 安装编译工具
# Linux:
sudo apt install gcc python3-dev

# macOS:
xcode-select --install

# Windows: 安装 Microsoft C++ Build Tools
# 或使用预编译版本:
pip install python-levenshtein-wheels
```

### 问题 4: gh auth login 失败

**症状:**
```
error: authentication failed
```

**解决方案:**
```bash
# 1. 检查网络连接
curl https://github.com

# 2. 使用 token 登录
gh auth login --with-token < token.txt

# 3. 或使用 SSH
gh auth login --with-token --git-protocol ssh
```

### 问题 5: 虚拟环境激活失败 (Windows)

**症状:**
```
cannot be loaded because running scripts is disabled
```

**解决方案:**
```powershell
# 以管理员身份运行 PowerShell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

# 然后重新激活虚拟环境
venv\Scripts\activate
```

## 卸载

如果需要卸载工具：

```bash
# 1. 停用虚拟环境
deactivate

# 2. 删除虚拟环境
rm -rf venv

# 3. 删除项目目录
cd ..
rm -rf github-pr-analyzer

# 4. （可选）卸载 GitHub CLI
# Ubuntu/Debian:
sudo apt remove gh

# macOS:
brew uninstall gh
```

## 更新

更新到最新版本：

```bash
# 1. 激活虚拟环境
source venv/bin/activate

# 2. 拉取最新代码（如果使用 git）
git pull

# 3. 更新依赖
pip install --upgrade -r requirements.txt

# 4. 验证
python main.py --version
```

## Docker 安装（高级）

对于喜欢容器化的用户，可以创建 Dockerfile：

```dockerfile
FROM python:3.11-slim

# 安装系统依赖
RUN apt-get update && apt-get install -y \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# 安装 GitHub CLI
RUN curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | \
    dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg && \
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | \
    tee /etc/apt/sources.list.d/github-cli.list && \
    apt-get update && \
    apt-get install -y gh

# 设置工作目录
WORKDIR /app

# 复制项目文件
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# 入口点
ENTRYPOINT ["python", "main.py"]
```

构建和运行：
```bash
docker build -t gh-pr-analyzer .
docker run -it --rm -v $(pwd):/workspace gh-pr-analyzer
```

## 获取帮助

如果遇到其他安装问题：

1. 查看 [常见问题](USAGE.md#故障排查)
2. 检查 [GitHub Issues](https://github.com/yourusername/github-pr-analyzer/issues)
3. 提交新的 Issue

---

安装完成后，请查看 [USAGE.md](USAGE.md) 了解使用方法。
