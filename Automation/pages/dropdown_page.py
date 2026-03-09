from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from Automation.pages.base_page import BasePage

class DropdownPage(BasePage):

    dropdown = (By.ID,'dropdown')

    def __init__(self,driver):
        super().__init__(driver)

    def select_option_by_text(self,text):
       dropdown_element = self.driver.find_element(*self.dropdown)
       select = Select(dropdown_element)
       select.select_by_visible_text(text)

