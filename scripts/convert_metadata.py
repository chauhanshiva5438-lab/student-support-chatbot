import json
import pickle
from pathlib import Path

json_path = Path("data/processed/embeddings/metadata.json")
pkl_path = Path("data/processed/embeddings/metadata.pkl")

with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

with open(pkl_path, "wb") as f:
    pickle.dump(data, f)

print("Metadata converted successfully.")