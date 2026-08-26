from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.saucedemo.com/")
time.sleep(1)

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(1)

products= driver.find_elements(By.CLASS_NAME, "inventory_item")
product_count= len(products)

if product_count==6:
    print("Test Passed: All 6 Products are displayed")
else:
    print(f"Test Failed: Expected 6 products, found {product_count}")

driver.quit()
