# test_phase5.py
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from tools.vector_store import (
    index_repository,
    semantic_search
)

repo_path = r"D:\summer26\R&D\RepoMind"

print("Building embeddings...")
result = index_repository(repo_path)

print(result)

print("\nSearching...")
results = semantic_search(
    "How are repositories cloned?"
)
results = semantic_search(
    "clone github repository"
)

for doc, meta in zip(
    results["documents"][0],
    results["metadatas"][0]
):
    print("\nFILE:")
    print(meta["file"])

    print("\nCONTENT:")
    print(doc[:300])
print(results)