
from abc import ABC

from langchain_core.retrievers import BaseRetriever
from langchain_core.documents import Document
from langchain_community.document_loaders import DirectoryLoader
import glob
import bm25s
from langchain_text_splitters import Language, RecursiveCharacterTextSplitter
from stemmer import stemmer

class FileFinder():
    @staticmethod
    def search_md(directory: str) -> list[str]:
        """
        Search all .md files under the (directory) folder recursively, and
        return them in a list of strings (a list of paths).
        """
        return glob.glob(f'{directory}/**/*.md', recursive=True)

    @staticmethod
    def search_py(directory: str) -> list[str]:
        """
        Search all .py files under the (directory) folder recursively, and
        return them in a list of strings (a list of paths).
        """
        return glob.glob(f'{directory}/**/*.py', recursive=True)

    @staticmethod
    def search_all(directory: str) -> list[str]:
        """
        Get the paths of all md and py files in the given directory
        """
        md_docs = FileFinder.search_md(directory)
        py_docs = FileFinder.search_py(directory)
        return md_docs + py_docs


# class BM25Retriever(BaseRetriever):
#     max_chunk_size: int
#     documents: list[Document] = []
#     k: int = 5
#     _retriever: bm25s.BM25 = bm25s.BM25()
#     # md_splitter = RecursiveCharacterTextSplitter.from_language(
#     #     language=Language.MARKDOWN,
#     #     # chunk_size=max_chunk_size
#     # )

#     @classmethod
#     def from_document(cls, path: str = 'data/raw') -> None:
#         """
#         Create an instance from a list of lanchain Document objects
#         """
#         # Get documents
#         docs = BM25Retriever.load_documents(path)
#         print(docs[500].metadata['path'])

#         # Extract corups
#         corpus = [doc.page_content for doc in cls.documents]




#         pass

#     def _get_relevant_documents(self, query: str, **args) -> list[Document]:
#         pass

#     # def load_chunks

#     @staticmethod
#     def load_documents(path: str = 'data/raw') -> list[Document]:
#         """
#         Loads python and markdown documents from the given path,
#         including subfolders.
#         """
#         # Initialize return list
#         doc_list: list[Document] = []

#         # Find document paths
#         files = FileFinder.search_all(path)

#         # Add content to list
#         for file in files:
#             try:
#                 with open(file, 'r') as f:
#                     d_content = f.read()
#                     # Create doc object and append to list
#                     doc = Document(
#                         d_content,
#                         metadata={
#                             'path': file
#                         }
#                     )
#                     doc_list.append(doc)
#             except (
#                 FileNotFoundError,
#                 PermissionError,
#                 UnicodeDecodeError
#             ):
#                 # Skip this file if invalid
#                 pass

#         return doc_list
