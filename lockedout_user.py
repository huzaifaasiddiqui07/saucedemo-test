from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.saucedemo.com/")

time.sleep(1)

driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

time.sleep(1)
if "Sorry, this user has been locked out" in driver.page_source:
    print("Test Passed: Locked-out user correctly rejected")
else:
    print("Test Failed: Locked-out user was not rejected")

driver.quit()