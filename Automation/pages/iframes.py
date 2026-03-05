from selenium.webdriver.common.by import By
from Automation.pages.base_page import BasePage

def open_iframe(self, iframe_url):
    self.driver.get(iframe_url)


class IframePage(BasePage):

    iframe = (By.ID ,'mce_0_ifr')
    textbox = (By.ID,'tinymce')

    def __init__(self,driver):
        super().__init__(driver)

    def switch_to_editor(self):
       self.switch_to_frame(self.iframe)

    def enter_text(self,text):
        editor = self.driver.find_element(*self.textbox)
        editor.send_keys(text)






