from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.saucedemo.com/")
time.sleep(1)

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(1)

sort_dropdown = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
sort_dropdown.select_by_value("lohi")
time.sleep(1)

prices= driver.find_elements(By.CLASS_NAME, "inventory_item_price")

price_values= []
for x in prices:
    clean_price = x.text.replace("$", "")
    price_values.append(float(clean_price))

print(price_values)

if price_values==sorted(price_values):
    print("Test Passed: Products are sorted from low to high price")
else:
    print("Test Failed: Products are not in the correct order")

driver.quit()
