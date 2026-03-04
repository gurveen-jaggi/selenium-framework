
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
