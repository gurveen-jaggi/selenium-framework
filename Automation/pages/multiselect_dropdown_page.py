from selenium.webdriver.common.by import By
from Automation.pages.base_page import BasePage



class MultiSelectDropdownPage(BasePage):
    cars_dropdown = (By.ID, "cars")

    def __init__(self, driver):
        super().__init__(driver)

    def select_cars(self, cars):
        self.select_multiple_options(self.cars_dropdown, cars)



