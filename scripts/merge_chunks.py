import json
from pathlib import Path

CHUNKS_FOLDER = Path("data/processed/chunks")
OUTPUT_FILE = Path("data/processed/all_chunks.json")


def merge_chunks():

    all_chunks = []

    json_files = list(CHUNKS_FOLDER.glob("*.json"))

    print(f"Found {len(json_files)} chunk files\n")

    for file in json_files:

        with open(file, "r", encoding="utf-8") as f:

            chunks = json.load(f)

            all_chunks.extend(chunks)

        print(f"Merged : {file.name}")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:

        json.dump(all_chunks, f, indent=4, ensure_ascii=False)

    print("\nAll chunks merged successfully.")
    print(f"Total Chunks : {len(all_chunks)}")


if __name__ == "__main__":
    merge_chunks()