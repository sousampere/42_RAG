#!/usr/bin/python3

from src import LLM


try:
    import sys
    import fire
    from pydantic import ValidationError

    from src import IndexArguments
    from src import BM25sRetriever, RetrieverException
except (KeyboardInterrupt, EOFError):
    print('Exiting.')
    sys.exit(0)


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
            # Print invalid argument for indexing and quit
            print(f"[Error] Invalid argument: {e.errors()[0]['loc'][0]}. "
                  f"{e.errors()[0]['msg']}.", file=sys.stderr)
            sys.exit(1)

        try:
            retriever = BM25sRetriever()
            retriever.index(
                chunk_size=index_args.max_chunk_size,
                overlap=0.1
            )
        except RetrieverException as e:
            print(f"[Error]: {e}", file=sys.stderr)
            sys.exit(1)

        print('Ingestion complete! Indices saved under data/processed/')

    @staticmethod
    def answer(
            query: str,
            k: int = 10,
            model_name: str = 'Qwen/Qwen3-0.6B'
            ) -> None:
        # Verify context window
        if 

        # Create / load indexed data for retrieving
        retriever = BM25sRetriever()
        retriever.index(2000, 0.1)

        # Get search results for query
        results = retriever.retrieve(
            query=query,
            k=k,
            run_manager=None)

        # Initiate LLM
        llm = LLM(model_name=model_name)

        # Answer query using LLM
        answer = llm.generate_answer(results)
        print('Answer: ' + answer.answer)

        return None

if __name__ == '__main__':
    try:
        rag = RAGProcessor()
        fire.Fire(rag)
    except (KeyboardInterrupt, EOFError):
        print('Exiting.')
        sys.exit(0)
