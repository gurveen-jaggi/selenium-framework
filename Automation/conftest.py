import pytest
import os
from selenium import webdriver
from datetime import datetime


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


# Hook to capture screenshot on failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    # Check if test failed
    if rep.when == "call" and rep.failed:

        driver = item.funcargs.get("driver", None)

        if driver:
            # Create screenshots folder if not exists
            screenshots_dir = "screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)

            # Add timestamp so files don’t overwrite
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_name = f"{item.name}_{timestamp}.png"

            file_path = os.path.join(screenshots_dir, file_name)

            driver.save_screenshot(file_path)