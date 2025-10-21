# GitHub PR & Commit Analyzer

一个强大的命令行工具，用于智能收集、分析和总结 GitHub Pull Requests 和提交记录。支持基于关键词的智能搜索和 AI 驱动的分析功能。

## ✨ 主要特性

- 🔍 **智能搜索**：AI 驱动的关键词提取和智能 PR/Commit 搜索
- 📊 **数据收集**：自动收集开放和已合并的 PR，以及 merge commits
- 🔄 **Diff 查看**：完整的代码变更查看功能
- 🤖 **AI 分析**：集成 cursor-agent CLI，智能总结变更内容
- 📅 **日期时间显示**：全面的 PR 和 commit 日期时间信息
- 💼 **商用级品质**：完整的错误处理、日志记录和用户体验
- 🎨 **美观输出**：使用 Rich 库提供漂亮的终端输出
- ⚙️ **环境变量配置**：直接使用环境变量配置（无需配置文件）

## 📋 前置要求

在使用本工具之前，请确保已安装以下依赖：

### 必需依赖

1. **Python 3.8+**
   ```bash
   python --version  # 应该 >= 3.8
   ```

2. **Git**
   ```bash
   git --version
   ```

3. **GitHub CLI (gh)**
   ```bash
   # Ubuntu/Debian
   sudo apt install gh
   
   # macOS
   brew install gh
   
   # Windows
   choco install gh
   ```
   
   安装后需要登录：
   ```bash
   gh auth login
   ```

### 可选依赖

4. **cursor-agent CLI** (用于 AI 分析功能)
   - 如需使用 AI 分析功能，请提前部署 cursor-agent
   - 在 `.env` 文件中配置路径

## 🚀 安装

### 方法 1: 从源码安装

```bash
# 克隆或下载项目
cd github-pr-analyzer

# 安装依赖
pip install -r requirements.txt

# 或使用 setup.py 安装
pip install -e .
```

### 方法 2: 使用虚拟环境（推荐）

```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Linux/macOS:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt
```

## ⚙️ 配置

使用环境变量配置工具：

```bash
# AI 配置（可选）
export CURSOR_AGENT_PATH=/path/to/cursor-agent

# 默认设置（可选）
export DEFAULT_MONTHS=3
export DEFAULT_REPO_PATH=.
```

无需配置文件 - 直接设置环境变量即可！

## 📖 使用方法

### 基本命令

#### 1. 收集 PR 和 Commit

```bash
# 自动检测当前仓库
python main.py collect

# 指定仓库
python main.py collect --repo owner/repo

# 指定时间范围（月）
python main.py collect --months 6
```

#### 2. 搜索相关变更

```bash
# 基本搜索
python main.py search "bug fix authentication"

# 带 AI 分析
python main.py search "add new feature" --analyze

# 显示 diff
python main.py search "optimization" --show-diff

# 高级选项
python main.py search "refactor" \
  --repo owner/repo \
  --months 6 \
  --min-score 50 \
  --max-results 10 \
  --analyze
```

#### 3. 查看特定 PR

```bash
# 查看 PR 详情
python main.py view-pr 123

# 查看 PR 并进行 AI 分析
python main.py view-pr 123 --analyze

# 指定仓库
python main.py view-pr 123 --repo owner/repo
```

#### 4. 查看特定 Commit

```bash
# 查看 commit 详情
python main.py view-commit abc1234

# 查看并分析
python main.py view-commit abc1234 --analyze
```

#### 5. 交互模式

```bash
# 启动交互式界面
python main.py interactive
```

### 使用示例

#### 场景 1：查找与特定功能相关的所有变更

```bash
# 搜索与 "authentication" 相关的所有 PR 和 commit
python main.py search "authentication" --months 3 --analyze

# 输出：
# - 匹配的 PR 和 commit 列表（按相关性排序）
# - 每个变更的 AI 生成摘要
# - 可选择保存分析报告
```

#### 场景 2：审查最近的合并

```bash
# 收集并查看最近 3 个月的所有 merge
python main.py collect --months 3

# 然后搜索特定类型的变更
python main.py search "performance optimization" --show-diff
```

#### 场景 3：深入分析特定 PR

```bash
# 查看 PR #456 的完整信息
python main.py view-pr 456 --analyze

# 输出包括：
# - PR 基本信息
# - 完整的 diff
# - AI 分析：目的、影响、技术细节
```

## 🎯 功能详解

### 智能搜索

工具使用多种匹配策略：

1. **精确匹配**：关键词在标题/消息中完全匹配
2. **模糊匹配**：使用 fuzzy matching 算法
3. **多字段搜索**：在标题、描述、作者、标签等多个字段中搜索
4. **评分系统**：根据匹配质量给出 0-100 的分数

### AI 分析功能

当配置了 cursor-agent 时，工具可以：

1. **自动总结**：提取变更的核心目的和功能
2. **影响分析**：评估变更对代码库的影响
3. **技术分析**：深入分析技术实现细节
4. **批量分析**：一次分析多个相关变更

### Diff 查看

- 彩色语法高亮
- 上下文显示
- 文件列表查看
- 支持 PR diff 和 commit diff

## 🛠️ 开发

### 项目结构

```
github-pr-analyzer/
├── main.py                 # 程序入口
├── setup.py               # 安装配置
├── requirements.txt       # 依赖列表
├── .env.example          # 配置模板
├── .gitignore            # Git 忽略规则
├── README.md             # 本文档
└── src/
    ├── __init__.py
    ├── config.py         # 配置管理
    ├── utils.py          # 工具函数
    ├── pr_collector.py   # PR 收集模块
    ├── commit_collector.py  # Commit 收集模块
    ├── diff_viewer.py    # Diff 查看模块
    ├── matcher.py        # 智能匹配模块
    ├── ai_analyzer.py    # AI 分析模块
    └── cli.py            # 命令行界面
```

### 运行测试

```bash
# 基本功能测试
python main.py --help

# 检查依赖
python -c "from src.cli import check_prerequisites; check_prerequisites()"
```

## 📝 常见问题

### Q: 提示 "gh CLI not authenticated"
A: 运行 `gh auth login` 并按提示完成 GitHub 登录。

### Q: 找不到仓库
A: 确保在 Git 仓库目录内运行，或使用 `--repo owner/repo` 明确指定。

### Q: AI 分析不可用
A: 需要在 `.env` 文件中配置 `CURSOR_AGENT_PATH`。AI 功能是可选的。

### Q: 搜索结果太多/太少
A: 调整 `--min-score` 参数（降低以获得更多结果，提高以获得更精确结果）。

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

本项目采用 MIT 许可证 - 免费用于商业和个人用途。

## 🔗 相关资源

- [GitHub CLI 文档](https://cli.github.com/manual/)
- [GitPython 文档](https://gitpython.readthedocs.io/)
- [Rich 库文档](https://rich.readthedocs.io/)

## 📧 联系方式

如有问题或建议，请通过 Issue 联系我们。

---

**Enjoy analyzing! 🎉**
