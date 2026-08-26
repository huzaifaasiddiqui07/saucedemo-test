from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.saucedemo.com/")
time.sleep(2)

driver.find_element(By.ID, "login-button").click()

if "Epic sadface: Username is required" in driver.page_source:
    print("Test Passed: Error message displayed for empty fields")
else:
    print("Test Failed: No error message for empty fields")

driver.quit()
