# GitHub PR & Commit Analyzer - 项目概览

## 项目简介

GitHub PR & Commit Analyzer 是一个商用级别的命令行工具，用于智能收集、分析和总结 GitHub Pull Requests 和已提交的 merge commits。该工具支持基于关键词的智能搜索，并可集成 AI（cursor-agent CLI）进行深度分析。

## 核心功能

### 1. 数据收集
- ✅ 收集所有开放的 Pull Requests
- ✅ 收集指定时间范围内已合并的 Pull Requests（默认 3 个月）
- ✅ 收集 Git 仓库中的 merge commits
- ✅ 自动检测当前仓库或手动指定仓库
- ✅ 支持从 GitHub API 和本地 Git 仓库双源收集

### 2. 智能搜索
- ✅ 基于关键词的模糊匹配搜索
- ✅ 多字段搜索（标题、描述、作者、标签、提交信息）
- ✅ 智能评分系统（0-100 分）
- ✅ 可配置的最低匹配分数和结果数量
- ✅ 支持单关键词和多关键词组合搜索

### 3. Diff 查看
- ✅ 完整的代码变更 diff 查看
- ✅ 彩色语法高亮显示
- ✅ 支持 PR diff 和 commit diff
- ✅ 文件列表展示
- ✅ 可配置的显示行数限制

### 4. AI 分析
- ✅ 集成 cursor-agent CLI 进行智能分析
- ✅ 自动总结变更目的和影响
- ✅ 技术实现细节分析
- ✅ 影响范围和风险评估
- ✅ 批量分析多个 PR/commit
- ✅ 生成 Markdown 格式的分析报告

### 5. 用户界面
- ✅ 美观的终端输出（使用 Rich 库）
- ✅ 交互式命令行模式
- ✅ 多个子命令支持不同操作
- ✅ 进度指示器和状态提示
- ✅ 彩色编码的结果展示
- ✅ 表格化的搜索结果

## 技术架构

### 架构设计

```
┌─────────────────────────────────────────────────────────┐
│                    CLI Interface (cli.py)               │
│  - Command parsing and user interaction                 │
│  - Progress display and result formatting               │
└──────────────┬──────────────────────────────────────────┘
               │
        ┌──────┴───────┐
        │              │
┌───────▼──────┐  ┌───▼──────────┐
│ PR Collector │  │Commit Collec.│
│              │  │              │
│ - GitHub API │  │ - GitPython  │
│ - gh CLI     │  │ - Local repo │
└──────┬───────┘  └───┬──────────┘
       │              │
       └──────┬───────┘
              │
       ┌──────▼───────┐
       │   Matcher    │
       │              │
       │ - Fuzzy match│
       │ - Scoring    │
       └──────┬───────┘
              │
    ┌─────────┴─────────┐
    │                   │
┌───▼─────────┐  ┌──────▼────────┐
│ Diff Viewer │  │  AI Analyzer  │
│             │  │               │
│ - Syntax HL │  │ - cursor-agent│
│ - File list │  │ - Report gen  │
└─────────────┘  └───────────────┘
```

### 模块说明

#### src/config.py
- 配置管理
- 环境变量加载
- 配置验证

#### src/utils.py
- 通用工具函数
- 命令执行封装
- 日期处理
- 依赖检查

#### src/pr_collector.py
- Pull Request 收集
- GitHub API 交互
- gh CLI 调用
- PR 数据模型

#### src/commit_collector.py
- Git commit 收集
- GitPython 操作
- merge commit 检测
- Commit 数据模型

#### src/diff_viewer.py
- 代码变更查看
- diff 生成和格式化
- 语法高亮
- 文件比较

#### src/matcher.py
- 智能搜索和匹配
- 模糊匹配算法
- 评分系统
- 多关键词处理

#### src/ai_analyzer.py
- AI 分析集成
- cursor-agent 调用
- 提示词生成
- 报告生成

#### src/cli.py
- 命令行界面
- 子命令实现
- 交互模式
- 结果展示

## 依赖项

### 核心依赖
- **Python 3.8+**: 编程语言
- **Git**: 版本控制系统
- **GitHub CLI (gh)**: GitHub API 访问
- **cursor-agent**: AI 分析（可选）

### Python 包
- **click**: CLI 框架
- **rich**: 终端美化
- **GitPython**: Git 操作
- **requests**: HTTP 请求
- **python-dotenv**: 环境变量
- **fuzzywuzzy**: 模糊匹配
- **python-levenshtein**: 字符串距离
- **python-dateutil**: 日期处理

## 数据流

### 1. 数据收集流程

```
GitHub Repository
       │
       ├─→ gh CLI → PR Collector → PullRequest Objects
       │
       └─→ Git Clone/Local → Commit Collector → Commit Objects
```

### 2. 搜索流程

```
User Query
    │
    ↓
Matcher
    │
    ├─→ PR List ─→ Score & Filter
    │
    └─→ Commit List ─→ Score & Filter
                            │
                            ↓
                    Sorted Results
```

### 3. 分析流程

```
Selected PR/Commit
        │
        ├─→ Diff Viewer → Get Diff Content
        │                      │
        │                      ↓
        └─→ AI Analyzer ← Diff + Metadata
                    │
                    ↓
            Analysis Report
```

## 使用场景

### 场景 1: 版本发布准备
```bash
# 收集最近的变更
python main.py collect --months 1

# 搜索新功能
python main.py search "feature" --analyze

# 搜索 bug 修复
python main.py search "fix" --analyze

# 生成 release notes 基础材料
```

### 场景 2: 代码审查
```bash
# 查看特定 PR
python main.py view-pr 123 --analyze

# 深入了解：
# - PR 目的
# - 代码变更
# - 潜在影响
```

### 场景 3: 安全审计
```bash
# 搜索安全相关变更
python main.py search "security vulnerability CVE" \
  --months 6 \
  --analyze

# 生成安全变更报告
```

### 场景 4: 技术债务追踪
```bash
# 搜索重构和技术债务
python main.py search "refactor technical debt" \
  --months 6 \
  --analyze

# 了解技术债务处理情况
```

### 场景 5: 新成员培训
```bash
# 使用交互模式探索项目历史
python main.py interactive

# 搜索关键功能的实现
# 了解项目演进过程
```

## 项目特点

### 1. 商用级品质
- ✅ 完整的错误处理和异常管理
- ✅ 详细的日志记录和状态提示
- ✅ 输入验证和安全检查
- ✅ 优雅的错误恢复
- ✅ 用户友好的提示信息

### 2. 可扩展性
- ✅ 模块化设计，易于扩展
- ✅ 清晰的接口定义
- ✅ 支持自定义分析类型
- ✅ 可配置的评分权重
- ✅ 插件式 AI 集成

### 3. 性能优化
- ✅ 批量操作减少 API 调用
- ✅ 可配置的结果限制
- ✅ 进度指示器避免用户焦虑
- ✅ 合理的超时设置
- ✅ 增量数据收集

### 4. 用户体验
- ✅ 美观的终端输出
- ✅ 交互式和命令式双模式
- ✅ 丰富的使用示例
- ✅ 详细的文档和帮助
- ✅ 友好的错误提示

## 配置选项

### 环境变量（.env）

```bash
# cursor-agent 路径（可选）
CURSOR_AGENT_PATH=/path/to/cursor-agent

# 默认时间范围（月）
DEFAULT_MONTHS=3

# 默认仓库路径
DEFAULT_REPO_PATH=.
```

### 命令行参数

所有命令都支持：
- `--repo, -r`: 指定仓库
- `--months, -m`: 时间范围
- `--help`: 显示帮助

搜索命令额外支持：
- `--min-score`: 最低匹配分数
- `--max-results`: 最大结果数
- `--analyze, -a`: 启用 AI 分析
- `--show-diff, -d`: 显示 diff

## 安全考虑

### 1. 认证和授权
- 使用 gh CLI 的官方认证机制
- 不存储或传输凭证
- 依赖 GitHub 的权限系统

### 2. 数据安全
- 本地处理，不上传到第三方
- 环境变量管理敏感信息
- .gitignore 排除配置文件

### 3. 代码安全
- 参数化命令执行
- 输入验证和清理
- 异常捕获和处理
- 安全的文件操作

## 性能指标

### 典型操作耗时
- 收集 100 个 PR: ~10-20 秒
- 收集 500 个 commit: ~5-10 秒
- 搜索匹配: ~1-2 秒
- 单个 diff 查看: ~1-3 秒
- 单个 AI 分析: ~10-30 秒（取决于 cursor-agent）

### 资源占用
- 内存: ~50-200 MB（取决于数据量）
- CPU: 低到中等（搜索和分析时较高）
- 网络: 中等（收集数据时）
- 磁盘: 最小（仅日志和报告）

## 未来规划

### 短期（v1.1）
- [ ] 支持更多 Git 平台（GitLab, Bitbucket）
- [ ] 高级过滤选项（标签、作者、日期范围）
- [ ] JSON/CSV 导出功能
- [ ] 缓存机制提升性能

### 中期（v1.5）
- [ ] Web 界面
- [ ] 插件系统
- [ ] 多仓库批量分析
- [ ] 可视化统计图表

### 长期（v2.0）
- [ ] 自定义报告模板
- [ ] CI/CD 集成
- [ ] 团队协作功能
- [ ] 机器学习驱动的推荐

## 贡献指南

欢迎贡献！请遵循以下步骤：

1. Fork 项目
2. 创建特性分支
3. 编写代码和测试
4. 提交 Pull Request
5. 等待审查

## 许可证

MIT License - 免费用于商业和个人用途

## 联系方式

- 问题反馈: GitHub Issues
- 功能建议: GitHub Discussions
- 邮件: 待定

---

**Built with ❤️ for the developer community**
