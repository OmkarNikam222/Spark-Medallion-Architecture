from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

RAW_PATH = PROJECT_ROOT / "storage" / "raw"

BRONZE_PATH = PROJECT_ROOT / "storage" / "bronze"

SILVER_PATH = PROJECT_ROOT / "storage" / "silver"

GOLD_PATH = PROJECT_ROOT / "storage" / "gold"

REJECTED_PATH = PROJECT_ROOT / "storage" / "rejected"