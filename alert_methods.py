from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.tutorialspoint.com/selenium/practice/alerts.php")

# Alert with OK
driver.find_element(By.ID, "alertBox").click()
time.sleep(1)
driver.switch_to.alert.accept()

# Alert with OK & Cancel
driver.find_element(By.ID, "confirmBox").click()
time.sleep(1)
driver.switch_to.alert.dismiss()

# Alert with Textbox
driver.find_element(By.ID, "promptBox").click()
time.sleep(1)
alert = driver.switch_to.alert
alert.send_keys("Test User")
alert.accept()

driver.quit()
