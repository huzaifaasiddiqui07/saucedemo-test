from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage

def test_checkout_error():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://www.saucedemo.com/")

        login_page=LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))).click()
        wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bike-light"))).click()
        wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"))).click()

        wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "shopping_cart_badge"), "3"))
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        wait.until(EC.presence_of_element_located((By.ID, "checkout")))
        wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

        wait.until(EC.visibility_of_element_located((By.ID, "first-name")))

        driver.find_element(By.ID, "first-name").send_keys("Huzaifa")
        driver.find_element(By.ID, "last-name").send_keys("Siddiqui")
        driver.find_element(By.ID, "continue").click()

        assert "Error: Postal Code is required" in driver.page_source
    finally:
        driver.quit() 