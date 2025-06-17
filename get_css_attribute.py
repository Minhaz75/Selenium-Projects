from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.com")

element = driver.find_element(By.NAME, "q")

# Get CSS value
print("Font size:", element.value_of_css_property("font-size"))

# Get attribute
print("Title attribute:", element.get_attribute("title"))

driver.quit()