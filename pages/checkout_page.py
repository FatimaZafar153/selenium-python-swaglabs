from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    # Element locators
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CHECKOUT_BTN = (By.ID, "checkout")
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    FINISH_BTN = (By.ID, "finish")
    CONFIRMATION = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def go_to_cart(self):
        """Click the cart icon."""
        self.wait.until(EC.element_to_be_clickable(self.CART_ICON)).click()

    def click_checkout(self):
        """Click the checkout button inside the cart page."""
        self.wait.until(EC.element_to_be_clickable(self.CHECKOUT_BTN)).click()

    def fill_checkout_info(self, first, last, zip_code):
        """Fill the shipping form."""
        self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME_INPUT)).send_keys(first)
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(last)
        self.driver.find_element(*self.POSTAL_CODE_INPUT).send_keys(zip_code)
        self.driver.find_element(*self.CONTINUE_BTN).click()

    def finish_order(self):
        """Click the finish button to complete purchase."""
        self.wait.until(EC.element_to_be_clickable(self.FINISH_BTN)).click()

    def get_confirmation_text(self):
        """Return the success message after order completion."""
        return self.wait.until(EC.visibility_of_element_located(self.CONFIRMATION)).text
