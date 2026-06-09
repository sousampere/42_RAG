#!/usr/bin/python3

import sys
import fire
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.retrievers import BM25Retriever
from pydantic import ValidationError

from src import (IndexArguments)
from src.index import FileFinder


class RAGProcessor:
    @staticmethod
    def index(max_chunk_size: int = 2000, index_target_folder: str = 'data/raw') -> None:
        """
        Index CLI command for indexing the data in the data/raw folder.
        """
        # Validate arguments
        try:
            index_args = IndexArguments(max_chunk_size=max_chunk_size)
        except ValidationError as e:
            # Invalid argument for indexing
            print(f"Invalid argument: {e.errors()[0]['loc'][0]}, "
                  f"{e.errors()[0]['msg']}", file=sys.stderr)
            sys.exit(1)

        # Inform user that the process is starting
        print(f"Indexing with chunks of {index_args.max_chunk_size}...")

        # 1. Charger tous les fichiers d'un dossier (ex: des fichiers .txt)
        loader = DirectoryLoader('./data/raw', glob="**/*.md", loader_cls=TextLoader)
        documents = loader.load()

        # 2. Découper le texte en morceaux (chunks) adaptés
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50, add_start_index=True)
        chunks = text_splitter.split_documents(documents)

        # 3. Initialiser le retriever avec les morceaux de texte
        # C'est ici que l'indexation "en mémoire" se fait
        retriever = BM25Retriever.from_documents(chunks)
        retriever.k = 1

        # 4. Utiliser le retriever
        resultats = retriever.invoke("How to instantiate an LLM ?")


        print(resultats[0].page_content)




if __name__ == '__main__':
    rag = RAGProcessor()
    fire.Fire(rag)
