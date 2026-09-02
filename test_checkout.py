from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_checkout():
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
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        time.sleep(1)

        driver.get("https://www.saucedemo.com/cart.html")
        wait.until(EC.element_to_be_clickable((By.ID, "checkout")))

        
        cart_items = driver.find_elements(By.CLASS_NAME, "cart_item")
        print("Items visible in cart:", len(cart_items))
        

        checkout_btn = driver.find_element(By.ID, "checkout")

        
        driver.execute_script("arguments[0].click();", checkout_btn)
        

        time.sleep(1)
        print("URL after clicking checkout:", driver.current_url)
        driver.save_screenshot("after_checkout_click.png")

        wait.until(EC.presence_of_element_located((By.ID, "first-name")))

        driver.find_element(By.ID, "first-name").send_keys("Huzaifa")
        driver.find_element(By.ID, "last-name").send_keys("Siddiqui")
        driver.find_element(By.ID, "postal-code").send_keys("74000")
        driver.find_element(By.ID, "continue").click()
        time.sleep(1)

        wait.until(EC.element_to_be_clickable((By.ID, "finish")))
        driver.find_element(By.ID, "finish").click()
        time.sleep(1)

        assert "Thank you for your order!" in driver.page_source
    finally:
        driver.quit()