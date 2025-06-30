from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://www.tutorialspoint.com/selenium/practice/droppable.php")
driver.maximize_window()
driver.implicitly_wait(10)

source = driver.find_element(By.ID, "draggable")
target = driver.find_element(By.ID, "droppable")

action = ActionChains(driver)
action.drag_and_drop(source, target).perform()

time.sleep(2)
driver.quit()
