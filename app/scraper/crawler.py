from selenium import webdriver
from selenium.webdriver.common.by import By  # type: ignore
import time
import json
from pathlib import Path
# ----------------------------
# STEP 1: Open Homepage
# ----------------------------

driver = webdriver.Chrome()

homepage = "https://www.webkeyindia.com/"



driver.get(homepage)

time.sleep(5)

# ----------------------------
# STEP 2: Collect All Links
# ----------------------------

links = driver.find_elements(By.TAG_NAME, "a")

all_urls = []

for link in links:

    href = link.get_attribute("href")

    if (
        href
        and "webkeyindia.com" in href
        and "#" not in href
        and "tel:" not in href
        and "mailto:" not in href
    ):
        all_urls.append(href)

# Remove duplicates
all_urls = list(set(all_urls))

print(f"\nTotal Unique URLs Found: {len(all_urls)}")



page_count = 0
pages = []

for url in all_urls:

    try:
        print(f"Scraping: {url}")

        driver.get(url)

        time.sleep(2)
        page_title = driver.title

        page_text = driver.find_element(
            By.TAG_NAME,
            "body"
        ).text

        pages.append({
        "url": url,
        "title": page_title,
        "content": page_text
})

        page_count += 1

    except Exception as e:

        print(f"Error scraping {url}")

# ----------------------------
# STEP 5: Finish
# ----------------------------

driver.quit()
output_file = Path("data/raw/pages.json")

output_file.parent.mkdir(parents=True, exist_ok=True)

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(
        pages,
        f,
        indent=4,
        ensure_ascii=False
    )

print(f"\nSaved {len(pages)} pages to {output_file}")

