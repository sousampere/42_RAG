#!/usr/bin/python3

import sys
import fire
from pydantic import ValidationError

from src import (IndexArguments,
                 BM25Retriever)
from src.index import FileFinder


class RAGProcessor:
    @staticmethod
    def index(max_chunk_size: int = 2000) -> None:
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

        # Search files to index
        INDEX_TARGET_FOLDER = 'data/raw'

        BM25Retriever().from_document(INDEX_TARGET_FOLDER)

        # Index markdown files


        # Index python files


        # Save index




if __name__ == '__main__':
    rag = RAGProcessor()
    fire.Fire(rag)
