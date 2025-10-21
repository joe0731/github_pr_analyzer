# GitHub PR Analyzer 使用指南

本文档提供详细的使用说明和最佳实践。

## 快速开始

### 1. 安装和配置

```bash
# 进入项目目录
cd github-pr-analyzer

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/macOS
# 或 venv\Scripts\activate  # Windows

# 安装依赖
pip install -r requirements.txt

# 配置环境变量
cp .env.example .env
# 编辑 .env 文件，配置 cursor-agent 路径（可选）
```

### 2. 验证安装

```bash
# 检查前置条件
python main.py collect --help

# 应该能看到命令帮助信息
```

## 命令详解

### collect - 收集数据

收集指定仓库的所有 PR 和 commit 数据。

```bash
# 基本用法（自动检测当前仓库）
python main.py collect

# 指定仓库
python main.py collect --repo nvidia/TensorRT-Model-Optimizer

# 自定义时间范围
python main.py collect --months 6

# 完整示例
python main.py collect --repo owner/repo --months 3
```

**输出示例：**
```
✓ Found 45 open PRs
✓ Found 123 merged PRs
✓ Found 89 merge commits
```

### search - 智能搜索

根据关键词搜索相关的 PR 和 commit。

```bash
# 基本搜索
python main.py search "fix memory leak"

# 带参数的搜索
python main.py search "add feature" \
  --repo owner/repo \
  --months 3 \
  --min-score 40 \
  --max-results 15

# 搜索并显示 diff
python main.py search "optimization" --show-diff

# 搜索并进行 AI 分析
python main.py search "refactor database" --analyze

# 完整功能（搜索 + diff + AI 分析）
python main.py search "authentication" \
  --analyze \
  --show-diff \
  --max-results 5
```

**参数说明：**
- `--repo, -r`: 指定仓库（格式：owner/repo）
- `--months, -m`: 搜索范围（月数），默认 3
- `--min-score`: 最低匹配分数（0-100），默认 30
- `--max-results`: 最大结果数量，默认 20
- `--analyze, -a`: 启用 AI 分析
- `--show-diff, -d`: 显示代码变更
- `--smart-search / --no-smart-search`: 使用 AI 智能搜索（默认：启用）

**输出示例：**
```
Search Results (8 matches)
┏━━━━┳━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━┓
┃ #  ┃ Type   ┃ ID         ┃ Title/Message        ┃ Author        ┃  Score ┃
┡━━━━╇━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━┩
│ 1  │ PR     │ #123       │ Fix authentication   │ john-doe      │     85 │
│ 2  │ Commit │ abc1234    │ Update auth service  │ jane-smith    │     72 │
└────┴────────┴────────────┴──────────────────────┴───────────────┴────────┘
```

### view-pr - 查看 PR 详情

查看特定 PR 的完整信息。

```bash
# 基本用法
python main.py view-pr 123

# 指定仓库
python main.py view-pr 123 --repo owner/repo

# 查看并进行 AI 分析
python main.py view-pr 123 --analyze
```

**交互流程：**
1. 显示 PR 基本信息
2. 询问是否显示 diff
3. 如果指定了 --analyze，进行 AI 分析
4. 显示完整的分析结果

### view-commit - 查看 Commit 详情

查看特定 commit 的完整信息。

```bash
# 使用完整 SHA
python main.py view-commit abc123def456

# 使用短 SHA
python main.py view-commit abc123

# 带 AI 分析
python main.py view-commit abc123 --analyze
```

### interactive - 交互模式

启动交互式界面，提供友好的菜单式操作。

```bash
python main.py interactive
```

**交互模式功能：**
1. 搜索查询
2. 查看特定 PR
3. 查看特定 commit
4. 退出

**适用场景：**
- 不熟悉命令行参数
- 需要多次查询
- 探索式分析

## 使用场景示例

### 场景 1：发现与安全相关的所有变更

```bash
# 搜索安全相关的 PR 和 commit
python main.py search "security vulnerability fix CVE" \
  --months 6 \
  --min-score 50 \
  --analyze

# 查看生成的分析报告
# 报告会包含：
# - 所有安全相关的变更
# - 每个变更的详细分析
# - 影响范围和风险评估
```

### 场景 2：审查新员工的贡献

```bash
# 先收集数据
python main.py collect --months 3

# 然后在交互模式中搜索特定作者
python main.py interactive
# > 输入 "author:new-developer"
```

### 场景 3：准备版本发布说明

```bash
# 收集最近的 merge commits
python main.py collect --months 1

# 搜索 feature 相关的变更
python main.py search "feature" --analyze --max-results 30

# 搜索 bug fix 相关的变更
python main.py search "fix bug" --analyze --max-results 30

# 生成的报告可以作为 release notes 的基础
```

### 场景 4：代码审查准备

```bash
# 查看特定 PR 的完整信息
python main.py view-pr 456 --analyze

# 输出包括：
# - PR 描述和统计信息
# - 完整的代码 diff（带高亮）
# - AI 生成的技术分析
# - 潜在影响和风险评估
```

### 场景 5：技术债务分析

```bash
# 搜索 refactor 和 tech debt 相关的变更
python main.py search "refactor technical debt cleanup" \
  --months 6 \
  --analyze

# 生成报告，了解团队在技术债务上的投入
```

## AI 分析功能详解

### 配置 cursor-agent

1. 确保 cursor-agent CLI 已安装
2. 在 `.env` 文件中设置路径：
   ```
   CURSOR_AGENT_PATH=/usr/local/bin/cursor-agent
   ```

### 分析类型

工具支持三种分析类型（代码中可扩展）：

1. **summary（摘要）**：快速了解变更的目的和影响
2. **impact（影响分析）**：评估变更的影响范围和风险
3. **technical（技术分析）**：深入的技术实现细节

### 分析输出

AI 分析会生成：
- Markdown 格式的分析报告
- 结构化的信息（目的、影响、技术细节等）
- 可选的保存到文件功能

### 批量分析

```bash
# 搜索并分析前 10 个匹配项
python main.py search "optimization" --analyze --max-results 10

# 系统会：
# 1. 搜索匹配的 PR/commit
# 2. 逐个获取 diff
# 3. 调用 AI 进行分析
# 4. 显示所有分析结果
# 5. 询问是否保存报告
```

## 高级技巧

### 1. 组合多个关键词

```bash
# 使用引号包含多个关键词
python main.py search "performance optimization memory"

# 工具会匹配包含这些词的任何 PR/commit
```

### 2. 调整匹配灵敏度

```bash
# 更严格的匹配（更少但更精确的结果）
python main.py search "feature" --min-score 70

# 更宽松的匹配（更多但可能不太相关的结果）
python main.py search "feature" --min-score 20
```

### 3. 限制结果数量

```bash
# 只看最相关的 5 个结果
python main.py search "bug fix" --max-results 5
```

### 4. 时间范围控制

```bash
# 查看最近 1 个月的变更
python main.py search "feature" --months 1

# 查看最近 12 个月的变更
python main.py search "feature" --months 12
```

## 最佳实践

### 1. 定期收集数据

建议定期运行 collect 命令，了解仓库状态：
```bash
python main.py collect --months 3
```

### 2. 使用描述性的搜索词

好的搜索词示例：
- ✅ "authentication security token"
- ✅ "database migration schema"
- ✅ "API endpoint REST"

不好的搜索词：
- ❌ "fix"（太宽泛）
- ❌ "update"（太模糊）
- ❌ "a"（单字符）

### 3. 合理使用 AI 分析

AI 分析消耗资源，建议：
- 先搜索，筛选出最相关的结果
- 只对重要的 PR/commit 使用 AI 分析
- 使用 --max-results 限制分析数量

### 4. 保存分析报告

对于重要的分析，选择保存报告：
```bash
python main.py search "critical security" --analyze
# 当询问时选择 "Yes" 保存报告
```

报告文件命名格式：`pr_analysis_report_owner_repo.md`

### 5. 利用交互模式探索

当不确定要查找什么时，使用交互模式：
```bash
python main.py interactive
```

## 故障排查

### 问题：command not found: gh

**解决方案：**
```bash
# 安装 GitHub CLI
# Ubuntu/Debian:
sudo apt install gh

# macOS:
brew install gh

# 然后登录
gh auth login
```

### 问题：cannot detect repository

**解决方案：**
```bash
# 确保在 Git 仓库目录内
git remote -v

# 或明确指定仓库
python main.py collect --repo owner/repo
```

### 问题：AI analysis not available

**原因：** cursor-agent 未配置

**解决方案：**
1. 检查 cursor-agent 是否安装
2. 在 `.env` 中配置正确的路径
3. 测试 cursor-agent 是否可用

### 问题：搜索结果为空

**可能原因：**
- 关键词拼写错误
- min-score 设置太高
- 时间范围太小

**解决方案：**
```bash
# 降低 min-score
python main.py search "your-query" --min-score 20

# 扩大时间范围
python main.py search "your-query" --months 6
```

## 性能优化建议

### 1. 大型仓库

对于有大量 PR 的仓库：
```bash
# 限制时间范围
python main.py collect --months 1

# 限制搜索结果
python main.py search "query" --max-results 10
```

### 2. 网络问题

如果网络较慢：
- GitHub CLI 会自动处理重试
- 考虑减少 months 参数
- 分批次收集数据

### 3. AI 分析速度

AI 分析可能较慢：
- 使用 --max-results 限制数量
- 先搜索，再对精选结果进行分析
- 批量分析会显示进度

## 扩展和定制

### 自定义分析类型

可以在 `src/ai_analyzer.py` 中添加新的分析类型：

```python
# 添加新的分析类型
elif analysis_type == "security":
    task = """
Please perform a security analysis:
1. Are there any security implications?
2. Are credentials or secrets properly handled?
3. Are there any potential vulnerabilities?
"""
```

### 自定义评分权重

在 `src/matcher.py` 中调整字段权重：

```python
field_weights = {
    "title": 1.0,      # 标题权重最高
    "body": 0.8,       # 描述权重较高
    "author": 0.5,     # 作者权重中等
    "labels": 0.6,     # 标签权重中等
}
```

## 贡献和反馈

欢迎提交问题和改进建议！

---

更多信息请参考 [README.md](README.md)
