from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_add_to_cart():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.saucedemo.com/")
    wait = WebDriverWait(driver, 10)

    wait.until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    wait.until(EC.presence_of_element_located((By.ID, "add-to-cart-sauce-labs-backpack")))
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()

    cart_count = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    
    print(cart_count)
    assert cart_count == "3", f"Test Failed: Cart count is {cart_count}, expected 3"
    print("Test Passed: 3 items added to cart")
    driver.quit()


