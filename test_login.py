from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage

def test_valid_login():

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    driver.get("https://www.saucedemo.com")

    Login_page=LoginPage(driver)
    Login_page.login("standard_user", "secret_sauce")
    
    assert "inventory" in driver.current_url

    driver.quit()