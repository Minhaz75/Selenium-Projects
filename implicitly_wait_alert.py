from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)  # Implicit wait set to 10 seconds

driver.get("https://www.tutorialspoint.com/selenium/practice/alerts.php")

driver.find_element(By.ID, "alertBox").click()
alert = driver.switch_to.alert
alert.accept()

driver.quit()
