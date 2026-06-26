import os
from sentence_transformers import SentenceTransformer
import chromadb



def load_python_files(repo_path):

    files = []

    skip_dirs = {
        ".venv",
        "__pycache__",
        ".git",
        "chroma_db",
        "repos",
        "test_repo",
        "tests"
    }

    skip_prefixes = {
        "test"
    }

    for root, dirs, filenames in os.walk(repo_path):

        dirs[:] = [
            d for d in dirs
            if d not in skip_dirs
        ]

        for file in filenames:

            if not file.endswith(".py"):
                continue

            if any(
                file.startswith(prefix)
                for prefix in skip_prefixes
            ):
                continue

            files.append(
                os.path.join(root, file)
            )

    return files

from tools.code_intelligence import (
    extract_function_chunks
)


def chunk_file(file_path):

    chunks = extract_function_chunks(
        file_path
    )

    return chunks



_model = None

def get_model():
    global _model
    if _model is None:
        _model = SentenceTransformer("BAAI/bge-small-en-v1.5")
    return _model


from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DB_PATH = BASE_DIR / "chroma_db"

_client = None

def get_client():
    global _client
    if _client is None:
        _client = chromadb.PersistentClient(path=str(DB_PATH))
    return _client


def index_repository(  repo_path,
    collection_name):
    #print("start");
    files = load_python_files(repo_path)
    #print("loaded files from repository")
    #print(f"Found {len(files)} files")
    
    idx = 0
    collection = get_client().get_or_create_collection(collection_name)
    for file_path in files:

        #print(f"\nProcessing: {file_path}")

        chunks = chunk_file(file_path)

        for chunk in chunks:

            #print("Generating embedding...")

            embedding = get_model().encode(
                chunk["text"]
            ).tolist()

            #print("Saving to ChromaDB...")
            
            collection.add(
                ids=[ f"{collection_name}_{idx}"],
                embeddings=[embedding],
                documents=[chunk["text"]],
                metadatas=[
                {
                    "file": chunk["file"],
                    "type": chunk["type"],
                    "name": chunk["name"]
                }
]
            )
            #print("Saved chunk to ChromaDB")
            idx += 1

            #print(f"Stored chunk {idx}")
            
    return {

        
        "indexed_chunks": idx
    }

def semantic_search(
    question,collection_name,
    top_k=5
):

    collection = get_client().get_or_create_collection(
    collection_name
)

    query_embedding = get_model().encode(
        question
    ).tolist()

    
    results = collection.query(
        query_embeddings=[
            query_embedding
        ],
        n_results=top_k
    )

    return results