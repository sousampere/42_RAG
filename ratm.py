#!/usr/bin/python3

import sys
import fire
from pydantic import ValidationError

from src import IndexArguments


class RAGProcessor:
    @staticmethod
    def index(max_chunk_size: int = 2000) -> None:
        """
        Index CLI command for indexing the data in the data/raw folder.
        """
        try:
            index_args = IndexArguments(max_chunk_size=max_chunk_size)
        except ValidationError as e:
            # Invalid argument for indexing
            print(f"Invalid argument: {e.errors()[0]['loc'][0]}, "
                  f"{e.errors()[0]['msg']}", file=sys.stderr)
            sys.exit(1)
        print(f"Indexing with chunks of {index_args.max_chunk_size}...")


if __name__ == '__main__':
    rag = RAGProcessor()
    fire.Fire(rag)
