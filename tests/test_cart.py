from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_add_to_cart(driver):
    # Step 1: Login
    login = LoginPage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")

    # Step 2: Add product to cart
    inventory = InventoryPage(driver)
    inventory.add_backpack_to_cart()

    # Step 3: Check if cart shows 1 item
    count = inventory.get_cart_count()
    assert count == 1, f"Expected 1 item in cart, found {count}"
