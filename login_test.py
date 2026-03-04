from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.options import Options

chrome_options = Options()

# Disable Chrome password manager & breach alerts
chrome_options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False,
    "profile.password_manager_leak_detection": False
})

# Optional: suppress automation banner
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-notifications")

service = Service("C:/Users/SAHIBA/PycharmProjects/PythonProject/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://the-internet.herokuapp.com/login")



#driver.get("https://the-internet.herokuapp.com/login")
driver.find_element(By.NAME, "username").send_keys("tomsmith")
driver.find_element(By.NAME, "password").send_keys("SuperSecretPassword!")
#driver.find_element(By.CLASS_NAME, "oxd-button").click()

wait = WebDriverWait(driver, 10)
login_buttonn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type = 'submit']")))
login_buttonn.click()

driver.maximize_window()
time.sleep(5)