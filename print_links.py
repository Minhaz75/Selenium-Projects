from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://parabank.parasoft.com/parabank/")

links = driver.find_elements(By.TAG_NAME, "a")

for link in links:
    print(f"Text: {link.text} -> URL: {link.get_attribute('href')}")

driver.quit()