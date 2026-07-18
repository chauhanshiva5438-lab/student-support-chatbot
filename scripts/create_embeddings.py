import json
import numpy as np
from pathlib import Path
from sentence_transformers import SentenceTransformer

INPUT_FILE = Path("data/processed/all_chunks.json")

OUTPUT_FOLDER = Path("data/processed/embeddings")
OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

print("Step 1 : Loading Model...")
model = SentenceTransformer(MODEL_NAME)
print("Step 2 : Model Loaded")

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    chunks = json.load(f)
    print(f"Step 3 : Loaded {len(chunks)} chunks")

texts = [chunk["text"] for chunk in chunks]

print(f"Creating embeddings for {len(texts)} chunks...")

print("Step 4 : Creating Embeddings...")
BATCH_SIZE = 128

all_embeddings = []

print("Step 4 : Creating Embeddings...")

for i in range(0, len(texts), BATCH_SIZE):

    batch = texts[i:i+BATCH_SIZE]

    batch_embeddings = model.encode(
        batch,
        convert_to_numpy=True,
        show_progress_bar=False
    )

    all_embeddings.append(batch_embeddings)

    print(f"Processed {min(i+BATCH_SIZE, len(texts))}/{len(texts)}")

embeddings = np.vstack(all_embeddings)
np.save(
    OUTPUT_FOLDER / "embeddings.npy",
    embeddings
)

with open(
    OUTPUT_FOLDER / "metadata.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(chunks, f, indent=4, ensure_ascii=False)

print("\nEmbeddings Saved Successfully!")
print("Shape :", embeddings.shape)