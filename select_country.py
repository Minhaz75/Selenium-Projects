from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("https://demo.guru99.com/test/newtours/register.php?authuser=0")

# Country drop-down
country_select = Select(driver.find_element(By.NAME, "country"))
country_select.select_by_visible_text("BANGLADESH")

time.sleep(2)
driver.quit()