from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
driver.implicitly_wait(10)

# Fill in the form
driver.find_element(By.NAME, "firstname").send_keys("John")
driver.find_element(By.NAME, "lastname").send_keys("Doe")
driver.find_element(By.XPATH, "//input[@value='Male']").click()
driver.find_element(By.XPATH, "//input[@value='2']").click()

# Select profession (checkbox)
driver.find_element(By.ID, "profession-1").click()

# Tools (checkbox)
driver.find_element(By.ID, "tool-2").click()

# Continent (dropdown)
Select(driver.find_element(By.ID, "continents")).select_by_visible_text("Europe")

# Selenium Commands (multi-select)
Select(driver.find_element(By.ID, "selenium_commands")).select_by_visible_text("Wait Commands")

# Submit the form
driver.find_element(By.ID, "submit").click()

time.sleep(2)
driver.quit()

