from driver_factory import get_driver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
import time

def test_sort_price_low_to_high():
    driver = get_driver()

    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    time.sleep(1)

    inventory_page = InventoryPage(driver)
    inventory_page.sort_by("lohi")

    time.sleep(1)
    prices = inventory_page.get_all_prices()

    assert prices == sorted(prices)

    driver.quit()
