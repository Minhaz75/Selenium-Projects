from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.tutorialspoint.com/selenium/practice/frames.php")

# Switch to frame by ID
driver.switch_to.frame("iframe_a")
driver.find_element(By.TAG_NAME, "input").send_keys("Inside Frame")
driver.switch_to.default_content()

driver.quit()
