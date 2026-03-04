import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


# -------------------- CHROME OPTIONS --------------------
chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False,
    "profile.password_manager_leak_detection": False
})
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-notifications")

service = Service("C:/Users/SAHIBA/PycharmProjects/PythonProject/chromedriver.exe")
driver =webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()

wait = WebDriverWait(driver , 12)

driver.get("https://practicetestautomation.com/practice-test-login/")
driver.find_element(By.ID,"username").send_keys("student")
driver.find_element(By.ID, "password").send_keys("Password123")
driver.find_element(By.XPATH, "//button[contains(.,'Submit')]").click()


time.sleep(3)










