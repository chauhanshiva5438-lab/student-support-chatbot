import json
import time
import faiss
from pathlib import Path
from functools import lru_cache
from sentence_transformers import SentenceTransformer

from gemini_client import generate_answer

# ==========================================
# Paths
# ==========================================

INDEX_PATH = Path("data/vector_store/asu_index.faiss")
METADATA_PATH = Path("data/processed/embeddings/metadata.json")

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"


# ==========================================
# Embedding Model
# ==========================================

@lru_cache(maxsize=1)
def get_embedding_model():

    start = time.time()

    print("Loading Embedding Model...")

    model = SentenceTransformer(
        MODEL_NAME,
        device="cpu"
    )

    print(f"Embedding Model Loaded in {time.time() - start:.2f} sec")

    return model


# ==========================================
# FAISS Index
# ==========================================

@lru_cache(maxsize=1)
def get_faiss_index():

    start = time.time()

    print("Loading FAISS Index...")

    index = faiss.read_index(str(INDEX_PATH))

    print(f"FAISS Loaded in {time.time() - start:.2f} sec")

    return index


# ==========================================
# Metadata
# ==========================================

@lru_cache(maxsize=1)
def get_metadata():

    start = time.time()

    print("Loading Metadata...")

    with open(METADATA_PATH, "r", encoding="utf-8") as f:
        metadata = json.load(f)

    print(f"Metadata Loaded in {time.time() - start:.2f} sec")
    print(f"Loaded {len(metadata)} chunks")

    return metadata


# ==========================================
# Retrieve Context
# ==========================================

def retrieve_context(question, k=10):

    embedding_model = get_embedding_model()
    index = get_faiss_index()
    metadata = get_metadata()

    query_embedding = embedding_model.encode(
        [question],
        convert_to_numpy=True,
        normalize_embeddings=True
    ).astype("float32")

    distances, indices = index.search(query_embedding, k)

    context = []

    for idx in indices[0]:

        context.append(
            f"Source: {metadata[idx]['source']}\n\n{metadata[idx]['text']}"
        )

    return "\n\n".join(context)


# ==========================================
# Terminal Chat
# ==========================================

if __name__ == "__main__":

    total_start = time.time()

    print("\nArizona State University Chatbot Ready!\n")

    # First load (cache ban jayegi)
    get_embedding_model()
    get_faiss_index()
    get_metadata()

    print(f"\nTotal Startup Time : {time.time() - total_start:.2f} sec\n")

    while True:

        question = input("You : ")

        if question.lower() == "exit":
            break

        context = retrieve_context(question)

        answer = generate_answer(
            context,
            question
        )

        print("\nBot:\n")
        print(answer)

        print("\n" + "=" * 80 + "\n")