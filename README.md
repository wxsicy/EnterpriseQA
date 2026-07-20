# 企业内部知识库智能问答系统

基于 RAG（检索增强生成）架构的企业知识库问答系统，支持文档上传、向量化、智能问答等功能。

## 技术栈

前端：Vue 3 + Element Plus + Vite + ECharts
后端：Flask + LangChain + ChromaDB
大模型：小米 MiMo（mimo-v2.5-pro）+ 阿里云百炼嵌入模型（qwen3.7-text-embedding）
数据库：MySQL 8.0
向量库：ChromaDB（本地持久化）

## 功能特性

- 用户登录注册，支持管理员和普通用户两种角色
- 知识库管理：创建、编辑、删除知识库
- 文档管理：支持上传 txt、pdf、md、docx 格式文档，自动向量化
- 智能问答：基于 RAG 检索增强生成，回答时引用参考文档来源
- 对话历史：记录所有问答记录，支持按知识库和会话查看
- 数据统计：知识库数量、文档数量、问答次数等可视化展示

## 快速开始

### 1. 环境准备

- Python 3.9+
- Node.js 18+
- MySQL 8.0

### 2. 克隆项目

git clone https://github.com/wxsicy/EnterpriseQA.git
cd EnterpriseQA

### 3. 配置环境变量

cd server
cp .env.example .env

编辑 .env 文件，填入你自己的配置：

- LLM_API_KEY：大模型 API Key
- LLM_BASE_URL：大模型 API 地址
- LLM_MODEL：大模型名称
- EMBED_API_KEY：嵌入模型 API Key
- EMBED_BASE_URL：嵌入模型 API 地址
- EMBED_MODEL：嵌入模型名称
- MYSQL_PASSWORD：MySQL 密码

### 4. 初始化数据库

mysql -u root -p < server/sql/init.sql

默认测试账号：
- 管理员：admin / 123456
- 普通用户：user1 / 123456

### 5. 安装后端依赖并启动

cd server
pip install -r requirements.txt
python app.py

后端默认运行在 http://localhost:5000

### 6. 安装前端依赖并启动

新开一个终端：

cd client
npm install
npm run dev

前端默认运行在 http://localhost:3000

### 7. 使用

浏览器访问 http://localhost:3000，登录后即可使用。

## 项目结构

`
EnterpriseQA/
├── client/                    # 前端（Vue 3）
│   ├── src/
│   │   ├── api/               # API 请求封装
│   │   ├── components/        # 公共组件
│   │   ├── router/            # 路由配置
│   │   ├── stores/            # Pinia 状态管理
│   │   └── views/             # 页面视图
│   ├── package.json
│   └── vite.config.js
├── server/                    # 后端（Flask）
│   ├── models/                # 数据库模型
│   ├── routes/                # API 路由
│   ├── services/              # 核心服务（RAG、向量化、嵌入）
│   ├── utils/                 # 工具函数
│   ├── sql/                   # 数据库初始化脚本
│   ├── test_docs/             # 测试文档
│   ├── app.py                 # 应用入口
│   ├── config.py              # 配置文件
│   └── requirements.txt
├── .gitignore
└── README.md
`

## 支持的模型

本项目使用 OpenAI 兼容接口，理论上支持所有兼容 OpenAI API 格式的大模型服务：

- 小米 MiMo：https://api.xiaomimimo.com/v1
- 通义千问（DashScope）：https://dashscope.aliyuncs.com/compatible-mode/v1
- DeepSeek：https://api.deepseek.com
- OpenAI：https://api.openai.com/v1
- 硅基流动：https://api.siliconflow.cn/v1

## 注意事项

- .env 文件包含敏感信息，不会被提交到 Git
- 上传的文档和向量数据存储在 server/uploads 和 server/chroma_data 目录下，已在 .gitignore 中排除
- 文档上传和向量化需要嵌入模型 API 可用
- 智能问答需要大模型 API 可用