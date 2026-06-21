from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.webkeyindia.com/")

time.sleep(5)

print(driver.title)

links = driver.find_elements(By.TAG_NAME, "a")

print("Number of links:", len(links))

for link in links[:10]:
    print(link.get_attribute("href"))

driver.quit()