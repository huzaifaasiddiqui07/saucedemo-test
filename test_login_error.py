from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from pages.login_page import LoginPage

def test_login_error():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.saucedemo.com/")
    time.sleep(2)

    login_page=LoginPage(driver)
    login_page.click_login_button()

    assert "Epic sadface: Username is required" in driver.page_source, "Test Failed: Username required error message not found"
    print("Test Passed: Username required error message displayed")

    driver.quit()
