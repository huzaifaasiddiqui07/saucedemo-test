# SauceDemo Selenium Test Suite

Automated UI test scripts for **saucedemo.com** (https://www.saucedemo.com/), built with Python + Selenium WebDriver as part of a QA automation learning project.

## Tech Stack
- Python 3.14
- Selenium WebDriver
- Pytest
- Page Object Model — login page refactored into `pages/login_page.py`, shared across all tests that log in (more page objects planned)
- `webdriver-manager` (auto-installs matching ChromeDriver)

## Test Cases

1. test_login.py — Valid login with standard_user, verifies redirect to /inventory.html
2. test_login_error.py — Submitting the login form with empty fields shows the "Username is required" error
3. test_lockedout_user.py — locked_out_user is correctly blocked with the lockout error message
4. test_add_to_cart.py — Adding 3 products updates the cart badge count to 3
5. test_remove_item.py — Adding then removing an item clears the cart badge
6. test_product_count.py — Inventory page displays all 6 products
7. test_sorting.py — "Price (low to high)" sort actually returns prices in ascending order
8. test_checkout.py — Full checkout flow: add items → cart → fill shipping info → finish → confirmation message
9. test_checkout_error.py — Checkout form correctly blocks submission when postal code is missing

## How to Run

Run any test file with pytest:

```
python -m pytest test_login.py -v
```

Add `-v` for verbose output showing each test name and pass/fail status.

## Notes / Known Issues
1. `test_checkout.py`, `test_checkout_error.py`, and `test_remove_item.py` are wrapped in `try/finally` so the browser closes even if an assertion or element lookup fails partway through — these were the flakiest tests early on, and leftover browser windows from failed runs were likely part of that problem.
2. These same three files use `WebDriverWait` + `expected_conditions` for reliability. The remaining tests (`test_login.py`, `test_add_to_cart.py`, `test_product_count.py`, `test_sorting.py`, `test_lockedout_user.py`) still use fixed `time.sleep()` delays and could be upgraded the same way.

## Next Steps
- Build out more page objects (inventory, cart, checkout pages) and migrate the rest of the tests to use them
- Add `try/finally` to the remaining tests that still don't have it
- Migrate remaining `time.sleep()`-based tests to explicit waits
- Add a shared `pytest` fixture for driver setup/teardown to cut down on repeated boilerplate across files