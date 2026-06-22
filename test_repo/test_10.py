import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from tools.repo_ingestion import (
    analyze_repository
)

print(

    analyze_repository(
        "https://github.com/kanika10-hub/SubSmart"
    )
)