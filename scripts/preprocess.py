import re
from pathlib import Path

RAW_FOLDERS = [
    Path("data/raw/pdf_text"),
    Path("data/raw/web")
]

OUTPUT_FOLDER = Path("data/processed/cleaned_text")
OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)


def clean_text(text):
    text = re.sub(r"\r", "", text)                 # Remove carriage returns
    text = re.sub(r"\t", " ", text)                # Replace tabs with spaces
    text = re.sub(r" +", " ", text)                # Multiple spaces -> one space
    text = re.sub(r"\n{2,}", "\n\n", text)         # Multiple blank lines -> one
    return text.strip()


def process_folder(folder):
    for file in folder.glob("*.txt"):

        with open(file, "r", encoding="utf-8") as f:
            text = f.read()

        cleaned = clean_text(text)

        output_file = OUTPUT_FOLDER / file.name

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(cleaned)

        print(f"Cleaned: {file.name}")


def main():

    for folder in RAW_FOLDERS:
        process_folder(folder)

    print("\nAll files cleaned successfully.")


if __name__ == "__main__":
    main()