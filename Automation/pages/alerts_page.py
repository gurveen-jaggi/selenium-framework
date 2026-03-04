from selenium.webdriver.common.by import By
from Automation.pages.base_page import BasePage


def open(self, alert_url):
    self.driver.get(alert_url)

class AlertsPage(BasePage):

    # def __init__(self, driver):
    #     super().__init__(driver)

    SIMPLE_ALERT = (By.XPATH, "//button[text()='Click for JS Alert']")
    CONFIRM_ALERT = (By.XPATH, "//button[text()='Click for JS Confirm']")
    PROMPT_ALERT = (By.XPATH, "//button[text()='Click for JS Prompt']")

    def click_simple_alert(self):
     self.driver.find_element(*self.SIMPLE_ALERT).click()


    def click_confirm_alert(self):
        self.driver.find_element(*self.CONFIRM_ALERT).click()


    def click_prompt_alert(self):
        self.driver.find_element(*self.PROMPT_ALERT).click()