from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://www.google.com")
time.sleep(1)

driver.get("https://www.bing.com")
time.sleep(1)

driver.back()
time.sleep(1)

driver.forward()
time.sleep(1)

driver.refresh()
time.sleep(1)

driver.quit()