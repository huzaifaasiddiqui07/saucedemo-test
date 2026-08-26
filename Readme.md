# SauceDemo Selenium Test Suite

Automated UI test scripts for **saucedemo.com** (https://www.saucedemo.com/), built with Python + Selenium WebDriver as part of a QA automation learning project.

## Tech Stack
- Python 3.14
- Selenium WebDriver
- `webdriver-manager` (auto-installs matching ChromeDriver)

## Test Cases

1. login.py — Valid login with standard_user, verifies redirect to /inventory.html
2. login_error.py — Submitting the login form with empty fields shows the "Username is required" error
3. lockedout_user.py — locked_out_user is correctly blocked with the lockout error message
4. add_to_cart.py — Adding 3 products updates the cart badge count to 3
5. remove_item.py — Adding then removing an item clears the cart badge
6. product_count.py — Inventory page displays all 6 products
7. sorting.py — "Price (low to high)" sort actually returns prices in ascending order
8. checkout.py — Full checkout flow: add items → cart → fill shipping info → finish → confirmation message
9. checkout_error.py — Checkout form correctly blocks submission when postal code is missing

## How to Run
Each script is standalone:

```
python login.py
python checkout.py
```

Each prints `Test Passed: ...` or `Test Failed: ...` to the terminal.

## Notes / Known Issues
1. `checkout.py`, `checkout_error.py`, and `remove_item.py` have intermittent failures at different points — e.g. after clicking `checkout`, the cart-link, or the remove button, the next expected element or page state sometimes doesn't appear within the wait timeout. Root cause not fully confirmed yet — under investigation (possible site-side flakiness or an element being blocked/intercepted).
2. Newer scripts (`checkout.py`, `checkout_error.py`, `remove_item.py`) use `WebDriverWait` + `expected_conditions` for reliability; older scripts (`login.py`, `add_to_cart.py`, `product_count.py`, `sorting.py`, `test-lockedout_user.py`) still use fixed `time.sleep()` delays and could be upgraded the same way.

## Next Steps
- Resolve the intermittent `checkout.py` failure
- Migrate remaining `time.sleep()`-based scripts to explicit waits
- Consolidate into a single test suite (e.g. `pytest`) instead of standalone scripts