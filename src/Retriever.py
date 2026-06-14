
import bm25s
from langchain_core.callbacks.manager import CallbackManagerForRetrieverRun
from langchain_core.retrievers import BaseRetriever
from langchain_core.documents import Document
from langchain_text_splitters import Language, RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader, TextLoader
import hashlib

class RetrieverException(Exception):
    pass

class BM25sRetriever(BaseRetriever):
    """
    Lanchain Retriever using the BM25s python module.
    """
    _retriever: bm25s.BM25 | None = None
    _corpus: list[str] | None = None
    _documents: list[Document] | None = None

    def index(self, chunk_size: int, overlap: float) -> bm25s.BM25:
        """
        Load documents and index them using the BM25s retriever.
        """
        # Load chunked documents
        documents = self._load_documents(chunk_size, overlap)
        self._documents = documents

        # Create list of text
        corpus = [doc.page_content for doc in documents]
        self._corpus = corpus

        # Load previous index if already indexed
        try:
            signature = self._get_dataset_hash()
            retriever = bm25s.BM25.load(
                f'data/processed/{signature}',
                load_corpus=True
            )
            print('Loaded data !')
            self._retriever = retriever
            return retriever
        except FileNotFoundError:
            pass

        # Tokenize copus
        tokenized_corpus = bm25s.tokenize(corpus)

        # Index
        retriever = bm25s.BM25()
        retriever.index(tokenized_corpus)

        # Save index with corresponding dataset signature
        self._retriever = retriever
        folder_name = self._get_dataset_hash()
        retriever.save(f'data/processed/{folder_name}', corpus=corpus)

        return retriever

    def retrieve(
            self,
            query: str,
            run_manager: CallbackManagerForRetrieverRun,
            k: int = 5
            ) -> list[Document]:
        """
        Alternative function to _get_relevant_documents
        to get documents relevant to a query.
        """
        return self._get_relevant_documents(
            query,
            k,
            run_manager=run_manager
        )

    def _get_relevant_documents(
            self,
            query: str,
            k: int = 5,
            *,
            run_manager: CallbackManagerForRetrieverRun
            ) -> list[Document]:
        """
        Get documents relevant to a query.
        """
        # Raise error if retrieving invalid data
        if self._retriever is None:
            raise RetrieverException(
                'Tried to retrieve without prior indexing.'
            )
        if self._corpus is None or self._documents is None:
            raise RetrieverException(
                'Empty corpus or documents data.'
            )

        # Tokenize query
        tokenized_query = bm25s.tokenize(query)

        # Retrieve
        result = self._retriever.retrieve(
            tokenized_query, self._corpus, k=k)

        # Get corresponding Documents from retrieved texts
        documents = []
        for retrieved in result[0][0]:
            for chunk in self._documents:
                if chunk.page_content == retrieved:
                    documents.append(chunk)

        return documents

    def _load_documents_in_given_format(
            self,
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

    def _load_documents(self,
                       chunk_size: int,
                       overlap: float,
                       main_directory: str = './data/raw') -> list[Document]:
        """
        Method used to load markdown and python documents, chunk them
        and combine them into one single document type
        """
        md_files = self._load_documents_in_given_format(
            chunk_size,
            overlap,
            'md',
            Language.MARKDOWN,
            main_directory
        )
        py_files = self._load_documents_in_given_format(
            chunk_size,
            overlap,
            'py',
            Language.PYTHON,
            main_directory
        )

        return md_files + py_files

    def _get_dataset_hash(self) -> str:
        """
        Hash the content of the repo to save a signature
        and prevent reindexing content.
        """
        if self._corpus is None or self._documents is None:
            raise RetrieverException(
                'Empty corpus or documents data.'
            )

        # Create string containing full data
        full_text: str = ''
        for text in self._corpus:
            full_text += text

        # Hash data into a string
        hashed_data = hashlib.sha1(
            full_text.encode('utf-8')
        ).hexdigest()

        return hashed_data