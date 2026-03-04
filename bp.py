from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

# -------------------- CHROME OPTIONS --------------------
chrome_options = Options()
chrome_options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False,
    "profile.password_manager_leak_detection": False
})
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-notifications")

# -------------------- DRIVER SETUP --------------------
service = Service("C:/Users/SAHIBA/PycharmProjects/PythonProject/chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()

wait = WebDriverWait(driver, 10)

# -------------------- OPEN SITE --------------------
driver.get("https://marketplace.bellpost.com/en")

# -------------------- CLICK SIGN IN --------------------
signin_btn = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[.//text()[contains(.,'Sign In')]]")
    )
)
signin_btn.click()

# -------------------- ENTER PHONE NUMBER --------------------
phone_input = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//div[@role='dialog']//input[@type='tel']")
    )
)
phone_input.send_keys("9582321602")

# -------------------- CLICK CONTINUE --------------------
continue_btn = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[.//text()[contains(.,'Continue')]]")
    )
)
continue_btn.click()

# -------------------- HANDLE OTP (NEW LOGIC) --------------------
otp_input = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//div[@role='dialog']//input")
    )
)

# Focus OTP input
otp_input.click()
time.sleep(0.3)

# Clear OTP completely
otp_input.send_keys(Keys.CONTROL + "a")
otp_input.send_keys(Keys.BACKSPACE)
time.sleep(0.3)

# Enter OTP IN ONE GO (IMPORTANT FIX)
otp_input.send_keys("123456")

print("OTP entered successfully")

# -------------------- HOLD FOR OBSERVATION --------------------
time.sleep(20)
driver.quit()