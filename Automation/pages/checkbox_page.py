from selenium.webdriver.common.by import By
from Automation.pages.base_page import BasePage

class CheckboxPage(BasePage):

    checkbox_one = (By.ID,  "check-box-one")
    checkbox_two = (By.ID, "check-box-two")
    checkbox_three = (By.ID, "check-box-three")
    checkbox_four = (By.ID, "check-box-four")

    def __init__(self, driver):
        super().__init__(driver)

    def select_checkboxes(self, values):
        for value in values:
            locator = (By.XPATH, f"//label[contains(text(), '{value}')]")
            self.click(locator)
