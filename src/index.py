
from langchain_core.retrievers import BaseRetriever
from langchain_core.documents import Document

class BM25Retriever(BaseRetriever):
    def _get_relevant_documents(self, query: str, **args) -> list[Document]:
        pass