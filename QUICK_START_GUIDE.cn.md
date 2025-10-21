# GitHub PR Analyzer - 快速开始指南

## 5 分钟快速开始

### 步骤 1: 运行自动安装脚本

```bash
# 进入项目目录
cd github-pr-analyzer

# 运行快速开始脚本
./quick_start.sh
```

脚本会自动：
- ✅ 检查 Python、Git、gh CLI
- ✅ 验证 gh CLI 认证
- ✅ 创建虚拟环境
- ✅ 安装所有依赖
- ✅ 创建配置文件

### 步骤 2: 运行安装测试

```bash
python test_installation.py
```

如果看到 "All tests passed!"，说明安装成功！

### 步骤 3: 第一次使用

#### 尝试交互模式（推荐新手）

```bash
python main.py interactive
```

交互模式会引导你完成所有操作。

#### 或使用命令行模式

```bash
# 在当前 Git 仓库中搜索
python main.py search "bug fix"

# 查看特定 PR
python main.py view-pr 123
```

## 常用命令速查

### 收集数据
```bash
# 收集当前仓库的 PR 和 commit（最近 3 个月）
python main.py collect

# 收集指定仓库（6 个月）
python main.py collect --repo owner/repo --months 6
```

### 搜索
```bash
# 基本搜索
python main.py search "authentication"

# 带 AI 分析
python main.py search "security fix" --analyze

# 显示代码变更
python main.py search "refactor" --show-diff

# 完整功能
python main.py search "feature" \
  --analyze \
  --show-diff \
  --max-results 5
```

### 查看详情
```bash
# 查看 PR
python main.py view-pr 123 --analyze

# 查看 commit
python main.py view-commit abc1234 --analyze
```

## 配置 AI 分析（可选）

如果要使用 AI 分析功能：

1. 安装 cursor-agent CLI
2. 编辑 `.env` 文件：
```bash
CURSOR_AGENT_PATH=/path/to/cursor-agent
```

3. 在搜索或查看时添加 `--analyze` 参数

## 获取帮助

```bash
# 查看所有命令
python main.py --help

# 查看特定命令的帮助
python main.py search --help
python main.py collect --help
```

## 下一步

- 📖 阅读 [README.md](README.md) 了解所有特性
- 📚 查看 [USAGE.md](USAGE.md) 学习详细用法
- 🔧 参考 [INSTALL.md](INSTALL.md) 解决安装问题
- 🏗️ 阅读 [PROJECT_OVERVIEW.md](PROJECT_OVERVIEW.md) 了解架构

## 常见问题

**Q: 提示 "gh not authenticated"**  
A: 运行 `gh auth login` 登录 GitHub

**Q: 找不到仓库**  
A: 确保在 Git 仓库目录内，或使用 `--repo` 指定

**Q: 搜索没有结果**  
A: 尝试降低 `--min-score` 参数

---

**祝使用愉快！** 🎉

如有问题，请查看文档或提交 Issue。
