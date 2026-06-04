# 42 RAG — Specification Document

## ℹ️ 1. Project Overview

### What the subject is about

The goal of the project is to :

- **<ins>Ingest</ins>** : Create a searchable knowledge base like google

    > Read and process files from the vLLM repo
    > Chunk data in different ways for Python code and Markdown documentation
    > Create a searchable index using TF-IDF or BM25
    > Store these index for fast retrieval

- **<ins>Search</ins>** : Be able to type a question and get relevant code snippets / documentation for this question, using this knowledge base

- **<ins>Answer</ins>** : Answer the questions using an LLM (Qwen/Qwen3-0.6B) with the given documentation / code snippets

- **<ins>Evaluate</ins>** : Evaluate the retrieval system quality using recall@k metrics



Note : Read 