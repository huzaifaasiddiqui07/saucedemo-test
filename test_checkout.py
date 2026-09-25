from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage

def test_checkout():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://www.saucedemo.com/")

        login_page=LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))).click()
        wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bike-light"))).click()
        wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"))).click()
        
        driver.get("https://www.saucedemo.com/cart.html")
        wait.until(EC.element_to_be_clickable((By.ID, "checkout")))

        cart_items= wait.until(EC.visibility_of_all_elements_located((By. CLASS_NAME, "cart_item")))
        assert len(cart_items)==3 
        
        checkout_btn = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
        checkout_btn.click()

        wait.until(EC.visibility_of_element_located((By.ID, "first-name")))

        driver.find_element(By.ID, "first-name").send_keys("Huzaifa")
        driver.find_element(By.ID, "last-name").send_keys("Siddiqui")
        driver.find_element(By.ID, "postal-code").send_keys("74000")
        driver.find_element(By.ID, "continue").click()

        finish_btn = wait.until(EC.element_to_be_clickable((By.ID, "finish")))
        finish_btn.click()

        success_msg = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "complete-header")))
        assert "Thank you for your order!" in success_msg.text
    finally:
        driver.quit()