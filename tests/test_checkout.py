import time
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_page import CheckoutPage

def test_checkout_end_to_end(driver):
    # Step 1: Login
    login = LoginPage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")
    time.sleep(3)

    # Step 2: Add item to cart
    inventory = InventoryPage(driver)
    inventory.add_backpack_to_cart()
    time.sleep(3)

    # Step 3: Go to cart and proceed to checkout
    checkout = CheckoutPage(driver)
    checkout.go_to_cart()
    time.sleep(3)
    checkout.click_checkout()
    time.sleep(3)

    # Step 4: Fill form and finish order
    checkout.fill_checkout_info("Jenny", "Lopez", "12345")
    checkout.finish_order()
    time.sleep(3)

    # Step 5: Confirm success
    text = checkout.get_confirmation_text()
    assert "Thank you for your order!" in text
    time.sleep(2)
