"""
自定义DashScope嵌入类
兼容LangChain的Embeddings接口，直接调用DashScope API
"""
import requests
from typing import List
from langchain_core.embeddings import Embeddings


class DashScopeEmbeddings(Embeddings):
    """阿里云百炼DashScope嵌入模型封装"""

    def __init__(self, api_key: str, base_url: str, model: str):
        self.api_key = api_key
        # 确保URL以/v1结尾，然后拼接/embeddings
        self.url = base_url.rstrip('/') + '/embeddings'
        self.model = model

    def _call_api(self, texts: List[str]) -> List[List[float]]:
        """调用DashScope嵌入API"""
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        payload = {
            'model': self.model,
            'input': texts
        }
        resp = requests.post(self.url, json=payload, headers=headers, timeout=60)
        resp.raise_for_status()
        data = resp.json()

        # 按index排序确保顺序正确
        embeddings = sorted(data['data'], key=lambda x: x['index'])
        return [item['embedding'] for item in embeddings]

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """嵌入多个文档文本"""
        return self._call_api(texts)

    def embed_query(self, text: str) -> List[float]:
        """嵌入单个查询文本"""
        return self._call_api([text])[0]