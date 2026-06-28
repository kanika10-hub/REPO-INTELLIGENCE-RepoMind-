# RepoMind

> **AI-powered Repository Intelligence using MCP, RAG, and Multi-Agent Systems**

RepoMind is an AI-powered repository intelligence system that enables LLMs to understand entire codebases instead of relying on manually pasted code snippets.

Built on the **Model Context Protocol (MCP)**, RepoMind combines repository-aware tools, semantic retrieval, dependency analysis, and specialized AI agents to answer repository-specific questions grounded in the actual source code.

Simply provide a GitHub repository URL and start asking questions in natural language.

---

# Why RepoMind?

Understanding large repositories is one of the biggest productivity bottlenecks for developers.

Developers often spend hours:

* Exploring project structure
* Reading dozens of files
* Tracing dependencies
* Understanding function relationships
* Finding entry points
* Identifying where changes will have an impact
* Learning unfamiliar architectures

RepoMind automates this process by combining static analysis, semantic retrieval, dependency intelligence, and LLM reasoning.

---

# Key Features

## Repository Ingestion

* Clone GitHub repositories
* Extract repository metadata
* Detect frameworks
* Generate repository summaries
* Build repository trees
* Analyze folder purposes

---

## Repository Intelligence

Instead of treating repositories as plain text, RepoMind understands repository structure through static code analysis.

Capabilities include:

* Function extraction
* Class extraction
* Import analysis
* Entry point detection
* Repository exploration
* File summaries

---

## Semantic Repository Search

Built using:

* Sentence Transformers
* BAAI/bge-small-en-v1.5
* ChromaDB

Features:

* Function-level embeddings
* Semantic code retrieval
* Repository-aware search
* Context generation for LLMs

---

## Dependency Intelligence

RepoMind builds dependency graphs using Python AST.

Capabilities:

* Repository dependency mapping
* Dependency chains
* Module relationships
* Change impact estimation
* Code flow understanding

---

## Multi-Agent Architecture

Instead of one generic assistant, RepoMind routes queries to specialized agents.

Current agents include:

* Explanation Agent
* Contributor Onboarding Agent
* Bug Investigation Agent
* Impact Analysis Agent
* Repository QA Agent
* Repository Analysis Agent
* Orchestrator Agent

Each agent combines repository-aware tools with LLM reasoning for its specific task.

---

## Repository-Aware Question Answering

RepoMind uses Retrieval-Augmented Generation (RAG).

Workflow:

Repository

↓

Repository Ingestion

↓

Function Extraction

↓

Embedding Generation

↓

ChromaDB

↓

Semantic Retrieval

↓

Context Builder

↓

LLM

↓

Repository-Aware Answer

Example questions:

* What does this repository do?
* Where should a new contributor start?
* Explain the architecture.
* Where is this function used?
* What breaks if I modify this module?
* Which files are most critical?
* Summarize the README.

---

## Repository Memory

Previously analyzed repositories are automatically remembered.

Features:

* ChromaDB collections
* Repository session management
* No unnecessary re-indexing
* Instant querying of previously analyzed repositories

---

# MCP Integration

RepoMind is implemented as a FastMCP server.

Claude can directly invoke repository-aware tools instead of relying solely on its internal knowledge.

Current MCP capabilities:

* Repository analysis
* Semantic search
* Dependency intelligence
* Contributor onboarding
* Repository explanations
* Bug investigation
* Repository Q&A
* Impact analysis

---

# Architecture

GitHub Repository

↓

Repository Ingestion

↓

Static Code Analysis

↓

Dependency Graph

↓

Function Extraction

↓

Embedding Generation

↓

ChromaDB Vector Store

↓

Semantic Retrieval

↓

Specialized Agents

↓

LLM Reasoning

↓

Repository-Aware Answers

---

# Tech Stack

* Python
* FastMCP
* ChromaDB
* SentenceTransformers
* BAAI/bge-small-en-v1.5
* GitPython
* Google Gemini API
* Python AST
* NetworkX

---

# Example Questions

* What does this repository do?
* Explain the architecture.
* Where should a new contributor start?
* Summarize the README.
* Which files are connected to this module?
* What breaks if I modify this function?
* Show repository dependencies.
* Which files are most important?

---

# Current Status

✅ Repository cloning

✅ Repository ingestion

✅ Static code analysis

✅ Function-level embeddings

✅ Semantic retrieval

✅ ChromaDB integration

✅ Dependency graph generation

✅ Repository-aware RAG

✅ Multi-agent orchestration

✅ MCP integration

✅ Repository memory

🚧 Advanced impact analysis improvements

🚧 Cross-repository reasoning

---

# Future Roadmap

* Pull Request analysis
* Architecture visualization
* Cross-repository reasoning
* Automatic documentation generation
* Test impact prediction
* Repository health reports
* Code evolution tracking
