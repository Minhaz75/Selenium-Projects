from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.tutorialspoint.com/selenium/practice/browser-windows.php")

# Open new tab
driver.find_element(By.ID, "tabButton").click()
time.sleep(2)

# Switch to new tab
windows = driver.window_handles
driver.switch_to.window(windows[1])
print("New Tab Title:", driver.title)
driver.close()

# Switch back to original
driver.switch_to.window(windows[0])
driver.quit()
