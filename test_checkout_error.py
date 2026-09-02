from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_checkout_error():
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

        wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "shopping_cart_badge"), "2"))
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        wait.until(EC.presence_of_element_located((By.ID, "checkout")))
        driver.find_element(By.ID, "checkout").click()

        wait.until(EC.presence_of_element_located((By.ID, "first-name")))

        driver.find_element(By.ID, "first-name").send_keys("Huzaifa")
        driver.find_element(By.ID, "last-name").send_keys("Siddiqui")
        driver.find_element(By.ID, "continue").click()
        time.sleep(1)

        assert "Error: Postal Code is required" in driver.page_source
    finally:
        driver.quit() 