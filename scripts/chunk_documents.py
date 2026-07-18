import json
from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter

INPUT_FOLDER = Path("data/processed/cleaned_text")
OUTPUT_FOLDER = Path("data/processed/chunks")

OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1500,
    chunk_overlap=300
)


def chunk_file(file_path):

    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    chunks = text_splitter.split_text(text)

    output = []

    for i, chunk in enumerate(chunks):

        output.append({
            "chunk_id": i + 1,
            "source": file_path.name,
            "text": chunk
        })

    output_file = OUTPUT_FOLDER / f"{file_path.stem}.json"

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=4, ensure_ascii=False)

    print(f"{file_path.name} → {len(chunks)} chunks")


def main():

    files = list(INPUT_FOLDER.glob("*.txt"))

    print(f"\nFound {len(files)} files\n")

    for file in files:
        chunk_file(file)

    print("\nChunking Completed Successfully.")


if __name__ == "__main__":
    main()