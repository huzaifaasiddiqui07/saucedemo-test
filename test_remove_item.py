from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage

def test_remove_item_from_cart():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://www.saucedemo.com/")

        login_page=LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")
        
        wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))).click()

        badge= wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
        assert badge.text == "1"

        wait.until(EC.element_to_be_clickable((By.ID, "remove-sauce-labs-backpack"))).click()

        wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))

        badges = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
        assert len(badges) == 0
        print("Item removed from cart successfully. Cart is now empty.")
    finally:
        driver.quit()  