"""
项目配置文件
从 .env 文件加载敏感配置（API Key、数据库密码等）
"""
import os
from dotenv import load_dotenv

# 加载 .env 文件中的环境变量
load_dotenv(os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env'))


class Config:
    """基础配置类"""

    # Flask密钥，用于JWT签名
    SECRET_KEY = os.environ.get('SECRET_KEY', 'enterprise-qa-secret-key-2024')

    # MySQL数据库配置
    MYSQL_HOST = os.environ.get('MYSQL_HOST', '127.0.0.1')
    MYSQL_PORT = int(os.environ.get('MYSQL_PORT', 3306))
    MYSQL_USER = os.environ.get('MYSQL_USER', 'root')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', '')
    MYSQL_DATABASE = os.environ.get('MYSQL_DATABASE', 'db_enterprise_qa')

    # SQLAlchemy数据库连接URI
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}"
        f"@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}?charset=utf8mb4"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # JWT Token有效期（秒），默认24小时
    JWT_EXPIRATION = 86400

    # 大模型API配置（小米MiMo，OpenAI兼容接口）
    LLM_API_KEY = os.environ.get('LLM_API_KEY', '')
    LLM_BASE_URL = os.environ.get('LLM_BASE_URL', 'https://api.xiaomi.com/v1')
    LLM_MODEL = os.environ.get('LLM_MODEL', 'MiMo-V2.5-Flash')

    # 嵌入模型API配置（阿里云百炼，OpenAI兼容接口）
    EMBED_API_KEY = os.environ.get('EMBED_API_KEY', '')
    EMBED_BASE_URL = os.environ.get('EMBED_BASE_URL', '')
    EMBED_MODEL = os.environ.get('EMBED_MODEL', 'qwen3.7-text-embedding')

    # ChromaDB持久化存储路径
    CHROMA_PERSIST_DIR = os.environ.get(
        'CHROMA_PERSIST_DIR',
        os.path.join(os.path.dirname(os.path.abspath(__file__)), 'chroma_data')
    )

    # 文件上传配置
    UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')
    MAX_CONTENT_LENGTH = 50 * 1024 * 1024  # 最大上传文件大小：50MB
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'md', 'docx'}

    # 文档分块配置
    CHUNK_SIZE = 500        # 每个分块的字符数
    CHUNK_OVERLAP = 50      # 分块之间的重叠字符数

    # 向量化批处理配置
    EMBED_BATCH_SIZE = 10   # 每批发送给嵌入API的分块数量
    EMBED_MAX_RETRIES = 3   # 嵌入失败最大重试次数

    # RAG检索配置
    RETRIEVER_TOP_K = 4     # 检索返回的相似文档数量