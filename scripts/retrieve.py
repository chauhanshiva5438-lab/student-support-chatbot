import json
import faiss
import numpy as np
from pathlib import Path
from sentence_transformers import SentenceTransformer

INDEX_PATH = Path("data/vector_store/asu_index.faiss")
METADATA_PATH = Path("data/processed/embeddings/metadata.json")

MODEL_NAME = "BAAI/bge-small-en-v1.5"

print("Loading model...")
model = SentenceTransformer(MODEL_NAME)

print("Loading FAISS index...")
index = faiss.read_index(str(INDEX_PATH))

print("Loading metadata...")
with open(METADATA_PATH, "r", encoding="utf-8") as f:
    metadata = json.load(f)

query = input("\nAsk your question: ")

query_embedding = model.encode(
    [query],
    convert_to_numpy=True
).astype("float32")

faiss.normalize_L2(query_embedding)

k = 5

distances, indices = index.search(query_embedding, k)

print("\nTop Results\n")

for rank, idx in enumerate(indices[0], start=1):

    chunk = metadata[idx]

    print("=" * 80)
    print(f"Result {rank}")
    print(f"Source : {chunk['source']}")
    print()
    print(chunk["text"][:700])
    print()