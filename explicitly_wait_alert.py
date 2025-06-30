from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.tutorialspoint.com/selenium/practice/alerts.php")

driver.find_element(By.ID, "alertBox").click()

# Explicit wait for alert to be present
WebDriverWait(driver, 10).until(EC.alert_is_present())
alert = driver.switch_to.alert
alert.accept()

driver.quit()
