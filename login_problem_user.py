from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

# Login
driver.find_element(By.ID, "user-name").send_keys("problem_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(2)

if "inventory" in driver.current_url:
    # Add item to cart
    driver.find_element(By.CLASS_NAME, "inventory_item").find_element(By.TAG_NAME, "button").click()
    time.sleep(1)

    # Go to cart
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(1)

    # Checkout
    driver.find_element(By.ID, "checkout").click()
    time.sleep(1)
    driver.find_element(By.ID, "first-name").send_keys("Test")
    driver.find_element(By.ID, "last-name").send_keys("User")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()
    time.sleep(1)
    driver.find_element(By.ID, "finish").click()
    time.sleep(1)

    # Logout
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    time.sleep(1)
    driver.find_element(By.ID, "logout_sidebar_link").click()
else:
    print("Login failed or user restricted: problem_user")

driver.quit()
