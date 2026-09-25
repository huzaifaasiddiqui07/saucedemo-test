from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from pages.login_page import LoginPage

def test_sorting():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    wait= WebDriverWait(driver,10)
    try:
        driver.get("https://www.saucedemo.com/")
    
        login_page=LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        sort_dropdown = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "product_sort_container")))

        Select(sort_dropdown).select_by_value("lohi")

        prices= wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "inventory_item_price")))
        
        price_values= []
        for x in prices:
            clean_price = x.text.replace("$", "")
            price_values.append(float(clean_price))

        print(price_values)

        assert price_values == sorted(price_values), "Test Failed: Items are not sorted by price from low to high"
        print("Test Passed: Items are sorted by price from low to high")
    finally:
        driver.quit()
