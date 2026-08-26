from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait=WebDriverWait(driver, 10)

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

print("Current URL:", driver.current_url, flush=True)
driver.find_element(By.ID, "checkout").click()

wait.until(EC.presence_of_element_located((By.ID, "first-name")))

driver.find_element(By.ID, "first-name").send_keys("Huzaifa")
driver.find_element(By.ID, "last-name").send_keys("Siddiqui")
driver.find_element(By.ID, "postal-code").send_keys("74000")
driver.find_element(By.ID, "continue").click()
time.sleep(1)

wait.until(EC.element_to_be_clickable((By.ID, "finish")))

driver.find_element(By.ID, "finish").click()
time.sleep(1)

if "Thank you for your order!" in driver.page_source:
    print("Test Passed: Checkout process completed successfully")
else:
    print("Test Failed: Checkout process did not complete successfully")

driver.quit()