
from pathlib import Path

BASE = Path(__file__).resolve().parent
print(BASE)

RAW = BASE / "data" / "raw"
CLEAN = BASE / "data" / "clean"

print(RAW)
print(CLEAN)