from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    # Locators for elements on the inventory (products) page
    ADD_TO_CART_BTN = (By.ID, "add-to-cart-sauce-labs-backpack")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def add_backpack_to_cart(self):
        """
        Adds the backpack product to the cart by clicking the 'Add to cart' button.
        """
        self.wait.until(EC.element_to_be_clickable(self.ADD_TO_CART_BTN)).click()

    def open_cart(self):
        """
        Clicks on the cart icon in the top right corner.
        """
        self.wait.until(EC.element_to_be_clickable(self.CART_ICON)).click()

    def get_cart_count(self):
        """
        Gets the number of items in the cart (from the cart badge).
        """
        badge = self.wait.until(EC.visibility_of_element_located(self.CART_BADGE))
        return int(badge.text)
