from Automation.pages.checkbox_page import CheckboxPage
# from Automation.config.config import BASE_URL, VALID_USERNAME, VALID_PASSWORD

# def test_login_valid(driver):
#     login_page = LoginPage(driver)
#     login_page.open(BASE_URL)
#
#     login_page.login(VALID_USERNAME, VALID_PASSWORD)
#
#     message = login_page.get_flash_message()
#     assert "You logged into a secure area!" in message
#
# def test_invalid_login(driver):
#     login_page = LoginPage(driver)
#     login_page.open(BASE_URL)
#
#     login_page.login(VALID_USERNAME, VALID_PASSWORD)
#
#     message = login_page.get_flash_message()
#     assert "Your username is invalid!" in message


from Automation.pages.login_page import LoginPage
from Automation.pages.multiselect_dropdown_page import MultiSelectDropdownPage
from Automation.utils.config_reader import ConfigReader
from Automation.pages.alerts_page import AlertsPage
from Automation.pages.iframes import IframePage
from Automation.pages.custom_dropdown_page import CustomDropdownPage
from Automation.pages.dropdown_page import DropdownPage
from Automation.pages.checkbox_page import CheckboxPage
from Automation.pages.drag_and_drop import DragDropPage
from selenium.webdriver.common.by import By

def test_valid_login(driver):
    config = ConfigReader()

    login_page = LoginPage(driver)
    login_page.open(config.get("base_url"))

    login_page.login(
        config.get("valid_username"),
        config.get("valid_password")
    )

    message = login_page.get_flash_message()
    assert "You logged into a secure area!" in message

def test_invalid_login(driver):
    config = ConfigReader()

    login_page = LoginPage(driver)
    login_page.open(config.get("base_url"))

    login_page.login(
        config.get("invalid_username"),
        config.get("invalid_password")
    )
    message = login_page.get_flash_message()
    assert "Your username is invalid!" in message

def test_js_alert(driver):

    config = ConfigReader()
    driver.get(config.get("alert_url"))

    alerts_page = AlertsPage(driver)

    alerts_page.click_simple_alert()
    alerts_page.accept_alert()

def test_confirm_alert(driver):

    config = ConfigReader()
    driver.get(config.get("alert_url"))

    alerts_page = AlertsPage(driver)

    alerts_page.click_confirm_alert()
    alerts_page.dismiss_alert()

    # def test_prompt_alert(driver):
    #
    #     config = ConfigReader()
    #     driver.get(config.get("alert_url"))
    #
    #     alerts_page = AlertsPage(driver)
    #
    #     alerts_page.click_prompt_alert()
    #     alerts_page.send_text_to_alert("Hello Gurveen")

def test_prompt_alert(driver):
    config = ConfigReader()
    driver.get(config.get("alert_url"))
    alerts_page = AlertsPage(driver)
    alerts_page.click_prompt_alert()
    alert_text = alerts_page.get_alert_text()
    assert alert_text == "I am a JS prompt"
    alerts_page.send_text_to_alert("Hello")


def test_iframe_editor(driver):

    config = ConfigReader()
    driver.get(config.get("iframe_url"))
    page = IframePage(driver)
    page.switch_to_editor()
    page.enter_text("Learning Frames in Selenium for interviews")
    page.switch_to_default()

def test_select_dropdown(driver):
    config = ConfigReader()
    driver.get(config.get("select_dropdown_url"))
    page = DropdownPage(driver)
    page.select_option_by_text("Option 1")

def test_custom_dropdown_page(driver):
    config = ConfigReader()
    driver.get(config.get("custom_dropdown_url"))
    page = CustomDropdownPage(driver)
    page.select_title("Dr.")

def test_standard_multiselect_dropdown(driver):
    config = ConfigReader()
    driver.get(config.get("standard_multiselect_url"))
    pages = MultiSelectDropdownPage(driver)
    pages.select_cars(['Saab','Opel',"Audi"])

def test_multiple_checkboxes(driver):
    config = ConfigReader()
    driver.get(config.get("checkbox_page_url"))
    page = CheckboxPage(driver)
    page.select_checkboxes(["Check Box One","Check Box Three"])

def test_drag_drop(driver):
    config = ConfigReader()
    driver.get(config.get("drag_drop_url"))
    page = DragDropPage(driver)

    # switch to iframe FIRST
    page.switch_to_drag_frame()
    page.perform_drag_drop()