import pytest
from selenium import webdriver
import os

@pytest.fixture
def driver():
    """
    Pytest fixture that creates a browser instance, yields it to the test,
    and ensures it is closed afterward.
    """
    driver = webdriver.Chrome()  # or webdriver.Firefox() if you prefer
    driver.maximize_window()
    yield driver  # control goes to the test here
    driver.quit()  # teardown: always run after test finishes

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):

    # Run the actual test first and get the result
    outcome = yield
    rep = outcome.get_result()

    # Only take screenshot if test failed during execution (not setup)
    if rep.when == "call" and rep.failed:
        # Get the WebDriver instance from the test
        driver = item.funcargs.get("driver")
        if driver:
            # Create a screenshots folder if not exists
            screenshots_dir = os.path.join(os.getcwd(), "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)

            # Create a unique filename from test name
            test_name = item.name
            screenshot_file = os.path.join(screenshots_dir, f"{test_name}.png")

            # Take and save the screenshot
            driver.save_screenshot(screenshot_file)
            print(f"\n📸 Screenshot saved: {screenshot_file}")
