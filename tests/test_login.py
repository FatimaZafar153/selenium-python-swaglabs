import pytest
from pages.login_page import LoginPage

def test_login_basic(driver):
    """
    High-level test using the page object and fixture:
      - Load login page
      - Perform login with known good credentials
      - Verify that landing page shows "Products"
    """
    # Initialize page object with the shared driver
    login_page = LoginPage(driver)

    # Step 1: open the login page
    login_page.load()

    # Step 2: perform login
    login_page.login("standard_user", "secret_sauce")

    # Step 3: verify result
    title = login_page.get_title()
    assert title == "Products", f"Expected 'Products' after login, got '{title}'"

@pytest.mark.parametrize("user, pwd, expected_error_substring", [
    ("locked_out_user", "secret_sauce", "locked out"),  # locked out user
    ("standard_user", "wrong_password", "do not match"),  # wrong password
    ("", "", "Username is required")  # empty credentials
])
def test_invalid_login(driver, user, pwd, expected_error_substring):
    """
    Negative login test: incorrect credentials should show an error banner.
    """
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login(user, pwd)

    # Locate the error message banner that appears on failed login
    error_banner = driver.find_element_by_css_selector("h3[data-test='error']").text
    assert expected_error_substring in error_banner, f"Expected error containing '{expected_error_substring}', got '{error_banner}'"