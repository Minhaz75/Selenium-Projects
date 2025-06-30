from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://www.tutorialspoint.com/selenium/practice/buttons.php")
driver.maximize_window()
driver.implicitly_wait(10)

action = ActionChains(driver)

# Double Click
double_btn = driver.find_element(By.ID, "doubleClickBtn")
action.double_click(double_btn).perform()
time.sleep(1)

# Right Click
right_btn = driver.find_element(By.ID, "rightClickBtn")
action.context_click(right_btn).perform()
time.sleep(1)

driver.quit()
