import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from tools.ask_repo import ask_repo
print("here")
print(
    ask_repo(
        "How are GitHub repositories cloned?"
    )
)