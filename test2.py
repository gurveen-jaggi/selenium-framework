from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Get 3rd product price
third_price = driver.find_element(
    By.XPATH,
    "(//div[@class='inventory_item_price'])[3]"
)

print(f"Third product price: {third_price.text}")

driver.quit()
