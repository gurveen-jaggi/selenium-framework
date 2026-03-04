from selenium.webdriver.common.by import By
from Automation.pages.base_page import BasePage
from Automation.utils.logger import get_logger

logger = get_logger(__name__)

class LoginPage(BasePage):
    USERNAME = (By.ID ,"username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type = 'submit']")
    FLASH_MESSAGE = (By.ID,"flash")

    def open(self, url):
        self.driver.get(url)

    def login(self, username, password):
        logger.info("Entering username")
        self.send_keys(self.USERNAME, username)

        logger.info("Entering password")
        self.send_keys(self.PASSWORD, password)

        logger.info("Clicking login button")
        self.click(self.LOGIN_BUTTON)

    def get_flash_message(self):
        return self.get_text(self.FLASH_MESSAGE)