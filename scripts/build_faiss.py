import numpy as np
import faiss
from pathlib import Path

EMBEDDINGS_FILE = Path("data/processed/embeddings/embeddings.npy")

INDEX_FOLDER = Path("data/vector_store")
INDEX_FOLDER.mkdir(parents=True, exist_ok=True)

print("Loading embeddings...")

embeddings = np.load(EMBEDDINGS_FILE)

print(f"Loaded {embeddings.shape[0]} embeddings")

# FAISS float32 data expect karta hai
embeddings = embeddings.astype("float32")

embeddings = embeddings.astype("float32")

faiss.normalize_L2(embeddings)

dimension = embeddings.shape[1]

index = faiss.IndexFlatIP(dimension)

index.add(embeddings)

faiss.write_index(
    index,
    str(INDEX_FOLDER / "asu_index.faiss")
)

print("\nFAISS Index Created Successfully!")
print("Dimension :", dimension)
print("Total vectors :", index.ntotal)