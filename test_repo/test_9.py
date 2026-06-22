import sys
from pathlib import Path




ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from tools.ask_repo import ask_repo

from tools.impact_analysis import (
    impact_analysis,
    find_function_callers
)
from tools.impact_agent import impact_agent

repo = r"D:\summer26\R&D\RepoMind"

result = impact_analysis(
    repo,
    "clone_repo"
)

print(result)

print(
    find_function_callers(
        repo,
        "clone_repo"
    )
)

print("-----------------------  ------------------- -------------------")
print(
    impact_agent(
        r"D:\summer26\R&D\RepoMind",
        "clone_repo"
    )
)
