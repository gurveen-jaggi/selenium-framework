from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from operator import contains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()

service = Service("C:/Users/SAHIBA/PycharmProjects/PythonProject/chromedriver.exe")
driver = webdriver.Chrome(service=service , options = chrome_options)
#driver = webdriver.Chrome(options=chrome_options)

# Disable Chrome password manager & breach alerts
chrome_options.add_experimental_option("prefs", {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False,
    "profile.password_manager_leak_detection": False
})

# Optional: suppress automation banner
chrome_options.add_argument("--disable-infobars")
chrome_options.add_argument("--disable-notifications")
driver.get("https://marketplace.bellpost.com/en")
driver.maximize_window()

wait = WebDriverWait(driver,10)
signin_btn = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[.//text()[contains(.,'Sign In')]]")
    )
)

signin_btn.click()


phone_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type= 'tel']")))

phone_input.send_keys("9582321602")

continuation_avlbl = wait.until(
    EC.visibility_of_element_located(
        (By.XPATH, "//button[.//text()[contains(.,'Continue')]]")
    )
)

continuation_avlbl.click()


otp_input = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//div[@role='dialog']//input")
    )
)

# Focus OTP input
actions = ActionChains(driver)
actions.move_to_element(otp_input).click().perform()
time.sleep(0.5)

# Clear OTP completely (important)
actions = ActionChains(driver)
actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL)
actions.send_keys(Keys.BACKSPACE)
actions.perform()
time.sleep(0.3)


actions = ActionChains(driver)

for digits in "123456":
    actions.send_keys(digits)
    actions.pause(0.3)

actions.perform()



time.sleep(20)



#"//button[contains(text(),'Sign In')]"