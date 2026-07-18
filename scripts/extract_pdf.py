import fitz
from pathlib import Path

PDF_FOLDER = Path("data/raw/pdfs")
OUTPUT_FOLDER = Path("data/raw/pdf_text")

OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)


def extract_text_from_pdf(pdf_path):
    document = fitz.open(pdf_path)

    text = ""

    for page in document:
        text += page.get_text()

    document.close()

    return text


def main():

    pdf_files = list(PDF_FOLDER.glob("*.pdf"))

    print(f"\nFound {len(pdf_files)} PDF(s).\n")

    for pdf in pdf_files:

        print(f"Reading : {pdf.name}")

        text = extract_text_from_pdf(pdf)

        output_file = OUTPUT_FOLDER / f"{pdf.stem}.txt"

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(text)

        print(f"Saved : {output_file.name}\n")

    print("=" * 50)
    print("All PDFs Processed Successfully")
    print("=" * 50)


if __name__ == "__main__":
    main()