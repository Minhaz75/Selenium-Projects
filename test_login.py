# file: test_login.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class SauceDemoTest:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self, username, password):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()
        time.sleep(2)

    def close(self):
        self.driver.quit()

if __name__ == "__main__":
    test = SauceDemoTest()
    test.login("standard_user", "secret_sauce")
    test.close()

