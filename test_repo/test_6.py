import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from tools.vector_store import semantic_search

results = semantic_search(
    "clone github repository"
)

for meta in results["metadatas"][0]:
    print(meta["file"])