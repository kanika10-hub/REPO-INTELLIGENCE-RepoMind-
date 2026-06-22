# RepoMind

RepoMind is an AI-powered repository intelligence system that helps developers understand unfamiliar codebases through semantic search, code analysis, dependency mapping, and repository-aware question answering.

Instead of manually reading hundreds of files, developers can ask natural language questions about a repository and receive answers grounded in the actual source code.

---

## Problem

Understanding large repositories is time-consuming.

Developers often spend hours:

* Exploring project structure
* Finding entry points
* Tracing dependencies
* Understanding function relationships
* Searching for implementation details

RepoMind automates this process by combining static code analysis, vector search, and LLM-powered reasoning.

---

## Architecture

GitHub Repository

↓

Repository Ingestion

↓

Code Intelligence

↓

Dependency Analysis

↓

Function-Level Embeddings

↓

ChromaDB Vector Store

↓

Semantic Retrieval

↓

LLM Reasoning

↓

Repository-Aware Answers

---

## Features Implemented

### Phase 1 — Repository Explorer

Built tools for repository navigation and inspection.

Features:

* List files and directories
* Read file contents
* Search text across repositories
* Detect Python files
* Find entry points
* Generate directory structures
* Summarize files

Tools:

* `list_files()`
* `read_file()`
* `search_text()`
* `find_python_files()`
* `find_entry_points()`
* `get_directory_structure()`
* `get_file_summary()`

---

### Phase 2 — GitHub Repository Ingestion

Built repository cloning and metadata analysis.

Features:

* Clone public GitHub repositories
* Generate repository metadata
* Detect frameworks
* Generate repository summaries
* Analyze folder purposes
* Build repository trees

Tools:

* `clone_repo()`
* `repo_metadata()`
* `generate_repo_summary()`
* `detect_framework()`
* `get_folder_purposes()`
* `repo_tree()`

---

### Phase 3 — Code Intelligence

Implemented AST-based static analysis.

Extracts:

* Functions
* Classes
* Imports

Example metadata:

```json
{
  "type": "function",
  "name": "clone_repo",
  "file": "tools/github_tools.py"
}
```

This enables repository-level code understanding instead of simple text search.

---

### Phase 4 — Dependency Graph

Built repository dependency analysis.

Capabilities:

* Parse imports using Python AST
* Map file relationships
* Identify repository structure
* Detect dependency chains

Tool:

* `repository_dependencies()`

---

### Phase 5 — Semantic Search

Built vector-based repository retrieval.

Stack:

* SentenceTransformers
* BAAI/bge-small-en-v1.5
* ChromaDB

Workflow:

Repository

↓

Function Extraction

↓

Embedding Generation

↓

ChromaDB Storage

↓

Semantic Retrieval

Results:

* Function-level indexing
* 100+ code chunks indexed
* Repository-aware retrieval

---

### Phase 6 — Repository Question Answering

Built Retrieval-Augmented Generation (RAG) pipeline.

Workflow:

Question

↓

Semantic Search

↓

Context Builder

↓

Gemini

↓

Answer

Example:

Question:

"How are repositories cloned?"

Retrieved:

* clone_repo()
* clone_github_repo()

Generated a repository-specific explanation instead of a generic answer.

---

### Phase 7 — Impact Analysis (In Progress)

Current work:

* Function caller detection
* Change impact analysis
* Dependency tracing

Target use case:

"What breaks if I modify clone_repo()?"

---

## MCP Integration

RepoMind is built as an MCP (Model Context Protocol) server using FastMCP.

Current MCP capabilities:

* Repository exploration
* Code intelligence
* Dependency analysis
* Semantic retrieval
* Repository question answering

---

## Tech Stack

* Python
* FastMCP
* ChromaDB
* SentenceTransformers
* BAAI/bge-small-en-v1.5
* GitPython
* Gemini API
* AST (Static Analysis)

---

## Current Results

* Repository cloning pipeline operational
* Function-level code indexing implemented
* ChromaDB vector search integrated
* Repository-aware question answering working
* Dependency graph generation completed
* Impact analysis under development

Example query:

"How are repositories cloned?"

RepoMind successfully retrieves relevant functions from the indexed repository and generates an explanation grounded in the source code.


