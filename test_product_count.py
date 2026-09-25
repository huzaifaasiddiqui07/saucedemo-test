from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage

def test_product_count():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    wait= WebDriverWait(driver, 10)
    try:
        driver.get("https://www.saucedemo.com/")

        login_page=LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        products= wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item")))

        product_count= len(products)

        assert product_count == 6, f"Expected 6 products, but found {product_count}."
        print(f"Test Passed: Found {product_count} products on the page as expected.")
    finally:
        driver.quit()
