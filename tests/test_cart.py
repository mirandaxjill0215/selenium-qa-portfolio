from driver_factory import get_driver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
import time

def test_add_item_to_cart():
    driver = get_driver()
    driver.maximize_window()

    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    time.sleep(1)

    inventory_page = InventoryPage(driver)
    inventory_page.add_item_to_cart("sauce-labs-backpack")

    time.sleep(1)
    assert inventory_page.get_cart_count() == "1"

    inventory_page.go_to_cart()
    time.sleep(1)

    cart_page = CartPage(driver)
    assert "Sauce Labs Backpack" in cart_page.get_item_names()

    driver.quit()
