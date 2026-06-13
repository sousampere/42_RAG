
from abc import ABC
from json import load
from pydoc import text
from typing import Any
from sqlalchemy import over
from typing_extensions import Doc

from langchain_core.callbacks.manager import CallbackManagerForRetrieverRun
from langchain_core.retrievers import BaseRetriever
from langchain_core.documents import Document
from langchain_community.document_loaders import DirectoryLoader
import glob
import bm25s
from langchain_text_splitters import Language, RecursiveCharacterTextSplitter
from stemmer import stemmer
from langchain_community.document_loaders import DirectoryLoader, TextLoader

class BM25Retriever(BaseRetriever):
    def from_index(self, chunk_size: int, overlap: float) -> None:
        """
        Load documents and index them using the BM25s retriever.
        """
        documents = self.load_documents(chunk_size, overlap)

        print(documents[-1])

    def _get_relevant_documents(self, query: str, *, run_manager: CallbackManagerForRetrieverRun) -> list[Document]:
        return super()._get_relevant_documents(query, run_manager=run_manager)

    def load_documents_in_given_format(self,
                                        chunk_size: int,
                                        overlap: float,
                                        extension: str,
                                        language: Language,
                                        main_directory: str = './data/raw'
                                        ) -> list[Document]:
        """
        Method to load Documents from a given file format
        """
        # Load files
        loader = DirectoryLoader(main_directory, glob=f"**/*.{extension}", loader_cls=TextLoader)
        documents = loader.load()

        # Chunk files
        text_splitter = RecursiveCharacterTextSplitter.from_language(
            language=language,
            chunk_size=chunk_size,
            chunk_overlap=int(chunk_size * overlap),
            add_start_index=True)
        chunks = text_splitter.split_documents(documents)

        # Add 'end_index' key in metadata
        for doc in chunks:
            doc.metadata['end_index'] = \
                doc.metadata['start_index'] + len(doc.page_content)

        return chunks

    def load_documents(self,
                       chunk_size: int,
                       overlap: float,
                       main_directory: str = './data/raw') -> list[Document]:
        """
        Method used to load markdown and python documents, chunk them
        and combine them into one single document type
        """
        md_files = self.load_documents_in_given_format(
            chunk_size,
            overlap,
            'md',
            Language.MARKDOWN,
            main_directory
        )
        py_files = self.load_documents_in_given_format(
            chunk_size,
            overlap,
            'py',
            Language.PYTHON,
            main_directory
        )

        return md_files + py_files

        # Load .md files
        md_loader = DirectoryLoader(main_directory, glob="**/*.md", loader_cls=TextLoader)
        md_documents = md_loader.load()

        # Chunk .md files
        md_text_splitter = RecursiveCharacterTextSplitter.from_language(
            language=Language.MARKDOWN,
            chunk_size=chunk_size,
            chunk_overlap=int(chunk_size * overlap),
            add_start_index=True)
        md_chunks = md_text_splitter.split_documents(md_documents)

        # Load .py files
        py_loader = DirectoryLoader(main_directory, glob="**/*.py", loader_cls=TextLoader)
        py_documents = py_loader.load()

        # Chunk .py files
        py_text_splitter = RecursiveCharacterTextSplitter.from_language(
            language=Language.PYTHON,
            chunk_size=chunk_size,
            chunk_overlap=int(chunk_size * overlap),
            add_start_index=True)
        py_chunks = py_text_splitter.split_documents(py_documents)

        # Combine data
        combined_data = md_chunks + py_chunks

        # Add 'end_index' key in metadata
        for doc in combined_data:
            doc.metadata['end_index'] = \
                doc.metadata['start_index'] + len(doc.page_content)

        # Return .py and .md
        return combined_data
