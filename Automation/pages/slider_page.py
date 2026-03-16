from selenium.webdriver.common.by import By
from Automation.pages.base_page import BasePage

class SliderPage(BasePage):

    frame = (By.CLASS_NAME, "demo-frame")
    locator = (By.CLASS_NAME, "ui-slider-handle")

    def __init__(self,driver):
     super().__init__(driver)

    def switch_to_slider_frame(self):     # This is a method to move to frame. This will be executed first then the drag and drop will be performed
        self.switch_to_frame(self.frame)

    def move_slider_right(self, value):
        self.move_slider(self.locator,value)