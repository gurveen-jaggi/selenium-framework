
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
from Automation.utils.config_reader import ConfigReader
from Automation.pages.alerts_page import AlertsPage


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

def test_prompt_alert(driver):

    config = ConfigReader()
    driver.get(config.get("alert_url"))

    alerts_page = AlertsPage(driver)

    alerts_page.click_prompt_alert()
    alerts_page.send_text_to_alert("Hello Gurveen")

