# test_functions.py
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))


from tools.code_intelligence import (
    extract_classes
)

print(
    extract_classes(
        "server.py"
    )
)