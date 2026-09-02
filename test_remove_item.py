from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_remove_item_from_cart():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://www.saucedemo.com/")
        time.sleep(1)

        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(1)

        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        time.sleep(1)
        cart_count = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        print(f"Item added to cart successfully. Cart count: {cart_count}")
        time.sleep(1)

        driver.find_element(By.ID, "remove-sauce-labs-backpack").click()

        wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))

        badges = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
        assert len(badges) == 0, "Item was not removed from the cart successfully."
        print("Item removed from cart successfully. Cart is now empty.")
    finally:
        driver.quit()  