from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    # Locators centralized so if the page changes, you update only here
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    TITLE = (By.CSS_SELECTOR, ".title") # Appears after successful login

    def __init__(self, driver, timeout=10):
        """
        Store the driver and prepare an explicit wait helper.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def load(self, url="https://www.saucedemo.com/"):
        """
        Navigate to the login page.
        """
        self.driver.get(url)

    def login(self, username, password):
        """
        Perform login: wait for fields, enter credentials, and click login.
        """

        # Wait until username field is visible, then type
        self.wait.until(EC.visibility_of_element_located(self.USERNAME)).send_keys(username)
        # Wait until password field is visible, then type
        self.wait.until(EC.visibility_of_element_located(self.PASSWORD)).send_keys(password)
        # Wait until login button is clickable
        login_btn = self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON))
        # Sanity check: it should not be disabled
        assert not login_btn.get_attribute("disabled"), "Login button is disabled unexpectedly"
        # Click to submit
        login_btn.click()

    def get_title(self):
        """
        After login, get the title text to verify successful login.
        """
        return self.wait.until(EC.visibility_of_element_located(self.TITLE)).text
