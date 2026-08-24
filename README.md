# 企业内部知识库智能问答系统

基于 RAG（检索增强生成）架构的企业知识库问答系统，支持文档上传、向量化、智能问答等功能。

## 技术栈

- **前端**：Vue 3 + Element Plus + Vite + ECharts
- **后端**：Flask + LangChain + ChromaDB
- **大模型**：小米 MiMo（mimo-v2.5-pro）+ 阿里云百炼嵌入模型（qwen3.7-text-embedding）
- **数据库**：MySQL 8.0
- **向量库**：ChromaDB（本地持久化）

## 功能特性

- 用户登录注册，支持管理员和普通用户两种角色
- 知识库管理：创建、编辑、删除知识库
- 文档管理：支持上传 txt、pdf、md、docx 格式文档，自动向量化
- 智能问答：基于 RAG 检索增强生成，回答时引用参考文档来源
- 对话历史：记录所有问答记录，支持按知识库和会话查看
- 数据统计：知识库数量、文档数量、问答次数等可视化展示

## 功能展示

模块 1 — 用户登录
标题：用户登录
描述：支持管理员和普通用户两种角色登录，采用 JWT Token 认证，保障接口安全。
要点：
- 用户名密码登录，Token 自动管理
- 角色权限控制，管理员可访问后台管理
- 未登录自动跳转登录页
<img width="1751" height="1086" alt="屏幕截图 2026-08-24 095242" src="https://github.com/user-attachments/assets/dde63cba-a72a-4203-9b08-31acbe4ab360" />


模块 2 — 智能问答
标题：智能问答
描述：核心功能。用户选择知识库后输入问题，系统通过 RAG 流程检索相关文档并由大模型生成专业回答。
要点：
- 左侧选择知识库，右侧实时对话
- 回答附带参考文档来源，可追溯
- 支持多轮对话，按会话管理记录
<img width="2530" height="1348" alt="image" src="https://github.com/user-attachments/assets/d2991f73-b641-4365-b869-86f6ddc45dbb" />


模块 3 — 知识库管理
标题：知识库管理
描述：管理员可创建和管理多个知识库，每个知识库拥有独立的向量空间，实现数据隔离。
要点：
- 创建、编辑、删除知识库
- 查看每个知识库的文档数量和状态
- 支持启用/禁用知识库
<img width="2535" height="1059" alt="image" src="https://github.com/user-attachments/assets/9f7b4bd8-2029-4e48-83cd-229947cd8ab9" />


模块 4 — 文档管理
标题：文档管理
描述：上传企业内部文档，系统自动解析、分块并向量化存储到 ChromaDB，为问答提供知识支撑。
要点：
- 支持 txt、pdf、md、docx 四种格式
- 自动文本分块（500 字/块，50 字重叠）
- 分批 Embedding，带失败重试机制
<img width="2534" height="1087" alt="image" src="https://github.com/user-attachments/assets/28137dde-556c-40fa-85d4-196f70aea245" />


模块 5 — 数据统计
描述：可视化展示系统运行数据，帮助管理员了解知识库使用情况和问答活跃度。
要点：
- 知识库数量、文档总数、问答次数统计
- ECharts 图表展示趋势变化
- 用户活跃度与热门问题分析
<img width="2535" height="1221" alt="屏幕截图 2026-08-24 110909" src="https://github.com/user-attachments/assets/1dd2f870-5027-4fae-9748-786c5414c7b7" />


模块 6 — 用户管理
标题：用户管理
描述：管理员可管理系统用户账号，控制不同角色的访问权限。
要点：
- 用户列表与角色管理
- 新增、编辑、删除用户
- 管理员与普通用户权限隔离
<img width="2540" height="721" alt="image" src="https://github.com/user-attachments/assets/25a33b56-b732-4804-b186-680c67600a3e" />


## 快速开始

### 1. 环境准备

- Python 3.9+
- Node.js 18+
- MySQL 8.0

### 2. 克隆项目

```bash
git clone https://github.com/wxsicy/EnterpriseQA.git
cd EnterpriseQA
```

### 3. 配置环境变量

```bash
cd server
cp .env.example .env
```

编辑 `.env` 文件，填入你自己的配置：

| 变量 | 说明 |
|------|------|
| LLM_API_KEY | 大模型 API Key |
| LLM_BASE_URL | 大模型 API 地址 |
| LLM_MODEL | 大模型名称 |
| EMBED_API_KEY | 嵌入模型 API Key |
| EMBED_BASE_URL | 嵌入模型 API 地址 |
| EMBED_MODEL | 嵌入模型名称 |
| MYSQL_PASSWORD | MySQL 密码 |

### 4. 初始化数据库

```bash
mysql -u root -p < server/sql/init.sql
```

默认测试账号：

| 角色 | 用户名 | 密码 |
|------|--------|------|
| 管理员 | admin | 123456 |
| 普通用户 | user1 | 123456 |

### 5. 安装后端依赖并启动

```bash
cd server
pip install -r requirements.txt
python app.py
```

后端默认运行在 `http://localhost:5000`

### 6. 安装前端依赖并启动

新开一个终端：

```bash
cd client
npm install
npm run dev
```

前端默认运行在 `http://localhost:3000`

### 7. 使用

浏览器访问 `http://localhost:3000`，登录后即可使用。

## 项目结构

```
EnterpriseQA/
│
├── client/                          # 前端（Vue 3）
│   ├── src/
│   │   ├── api/                     # API 请求封装
│   │   ├── components/              # 公共组件
│   │   ├── router/                  # 路由配置
│   │   ├── stores/                  # Pinia 状态管理
│   │   └── views/                   # 页面视图
│   ├── package.json
│   └── vite.config.js
│
├── server/                          # 后端（Flask）
│   ├── models/                      # 数据库模型
│   ├── routes/                      # API 路由
│   ├── services/                    # 核心服务
│   │   ├── rag_service.py           # RAG 问答服务
│   │   ├── vector_service.py        # 文档向量化服务
│   │   └── embeddings.py            # 嵌入模型封装
│   ├── utils/                       # 工具函数
│   ├── sql/                         # 数据库初始化脚本
│   ├── test_docs/                   # 测试文档
│   ├── app.py                       # 应用入口
│   ├── config.py                    # 配置文件
│   └── requirements.txt
│
├── .env.example                     # 环境变量模板
├── .gitignore
└── README.md
```

## 支持的模型

本项目使用 OpenAI 兼容接口，理论上支持所有兼容 OpenAI API 格式的大模型服务：

| 服务商 | Base URL | 示例模型 |
|--------|----------|----------|
| 小米 MiMo | https://api.xiaomimimo.com/v1 | mimo-v2.5-pro |
| 通义千问 | https://dashscope.aliyuncs.com/compatible-mode/v1 | qwen-plus |
| DeepSeek | https://api.deepseek.com | deepseek-chat |
| OpenAI | https://api.openai.com/v1 | gpt-4o |
| 硅基流动 | https://api.siliconflow.cn/v1 | Qwen/Qwen2.5-7B-Instruct |

## 注意事项

- `.env` 文件包含敏感信息，不会被提交到 Git
- 上传的文档和向量数据存储在 `server/uploads` 和 `server/chroma_data` 目录下，已在 `.gitignore` 中排除
- 文档上传和向量化需要嵌入模型 API 可用
- 智能问答需要大模型 API 可用
