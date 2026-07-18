import pandas as pd
from pathlib import Path
from playwright.sync_api import sync_playwright

CSV_FILE = Path("data/sources.csv")
OUTPUT_FOLDER = Path("data/raw/web")

OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)


def scrape_page(url):
    with sync_playwright() as p:

        browser = p.chromium.launch(headless=True)

        page = browser.new_page()

        page.goto(url, wait_until="domcontentloaded", timeout=60000)

        text = page.locator("body").inner_text()

        browser.close()

        return text


def save_text(name, text):

    filename = name.lower().replace(" ", "_").replace("&", "and")

    with open(
        OUTPUT_FOLDER / f"{filename}.txt",
        "w",
        encoding="utf-8"
    ) as f:

        f.write(text)


def main():

    df = pd.read_csv(CSV_FILE)

    web_pages = df[df["type"] == "WEB"]

    print(f"Found {len(web_pages)} webpages.\n")

    for _, row in web_pages.iterrows():

        print(f"Scraping: {row['name']}")

        try:
            text = scrape_page(row["source"])
            save_text(row["name"], text)
            print("Done\n")

        except Exception as e:
            print(f"Failed: {row['name']}")
            print(e)


if __name__ == "__main__":
    main()