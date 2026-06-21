from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# ----------------------------
# STEP 1: Open Homepage
# ----------------------------

driver = webdriver.Chrome()

homepage = "https://www.webkeyindia.com/"

print("Opening homepage...")

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

driver.quit()

# ----------------------------
# STEP 3: Create Output File
# ----------------------------

with open("website_data.txt", "w", encoding="utf-8") as file:
    file.write("WEBKEY INDIA WEBSITE DATA\n")
    file.write("=" * 80 + "\n")

# ----------------------------
# STEP 4: Scrape Each Page
# ----------------------------

driver = webdriver.Chrome()

page_count = 0

for url in all_urls:

    try:
        print(f"Scraping: {url}")

        driver.get(url)

        time.sleep(2)

        page_text = driver.find_element(
            By.TAG_NAME,
            "body"
        ).text

        with open(
            "website_data.txt",
            "a",
            encoding="utf-8"
        ) as file:

            file.write("\n\n")
            file.write("=" * 80)
            file.write("\n")

            file.write(f"URL: {url}\n")

            file.write("=" * 80)
            file.write("\n\n")

            file.write(page_text)

        page_count += 1

    except Exception as e:

        print(f"Error scraping {url}")

# ----------------------------
# STEP 5: Finish
# ----------------------------

driver.quit()

print("\nScraping Completed!")
print(f"Pages Scraped: {page_count}")
print("Data saved in website_data.txt")