from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def send_keys(self,locator, value):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(value)

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def accept_alert(self):
        alert = self.driver.switch_to.alert
        alert.accept()

    def dismiss_alert(self):
        alert = self.driver.switch_to.alert
        alert.dismiss()

    def get_alert_text(self):
        alert = self.driver.switch_to.alert
        return alert.text

    def send_text_to_alert(self,text):
        alert = self.driver.switch_to.alert
        alert.send_keys(text)
        alert.accept()

    def switch_to_frame(self, locator):
        frame = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(locator)
        )

        self.driver.switch_to.frame(frame)

    def switch_to_default(self):
        self.driver.switch_to.default_content()

    def select_from_search_dropdown(self, locator,value):

        dropdown = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(locator))
        dropdown.send_keys(value)
        dropdown.send_keys(Keys.RETURN)

    def select_multiple_options(self , locator, values):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

        select = Select(element)

        for val in values:
            select.select_by_visible_text(val)

    def hover(self, locator):
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)

        actions.move_to_element(element).perform()

    def right_click(self, locator):
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)

        actions.context_click(element).perform()

    def double_click(self, locator):
        element = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)

        actions.double_click(element).perform()

    def drag_and_drop(self, source_locator, target_locator):
        source = self.driver.find_element(*source_locator)
        target = self.driver.find_element(*target_locator)
        actions = ActionChains(self.driver)

        actions.drag_and_drop(source,target).perform()

    def drag_slider(self, locator, x_offset):
        slider = self.driver.find_element(*locator)
        actions = ActionChains(self.driver)

        actions.click_and_hold(slider).move_by_offset(x_offset,0).release().perform()




