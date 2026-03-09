from selenium.webdriver.common.by import By
from Automation.pages.base_page import BasePage

class CustomDropdownPage(BasePage):

    select_one_dropdown_container = (By.ID,"selectOne")
    dropdown_input = (By.ID, "react-select-3-input")

    def __init__(self,driver):
        super().__init__(driver)

    def select_title(self, title):

        self.click(self.select_one_dropdown_container)

        self.select_from_search_dropdown(self.dropdown_input, title)

