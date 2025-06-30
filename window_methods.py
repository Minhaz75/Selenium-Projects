from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.tutorialspoint.com/selenium/practice/browser-windows.php")

# Open new window
driver.find_element(By.ID, "windowButton").click()
time.sleep(2)

# Switch to new window
windows = driver.window_handles
driver.switch_to.window(windows[1])
print("New Window Title:", driver.title)
driver.close()

# Switch back to original
driver.switch_to.window(windows[0])
driver.quit()
