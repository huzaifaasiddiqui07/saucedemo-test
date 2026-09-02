from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_login_error():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)

    driver.find_element(By.ID, "login-button").click()

    assert "Epic sadface: Username is required" in driver.page_source, "Test Failed: Username required error message not found"
    print("Test Passed: Username required error message displayed")

    driver.quit()
