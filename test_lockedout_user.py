from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from pages.login_page import LoginPage

def test_locked_out_user():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.saucedemo.com/")

    time.sleep(1)

    login_page=LoginPage(driver)
    login_page.login("locked_out_user", "secret_sauce")

    time.sleep(1)
    assert "Epic sadface: Sorry, this user has been locked out." in driver.page_source, "Test Failed: Locked out user error message not found"

    driver.quit()