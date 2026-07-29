from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def add_item_to_cart(self, item_id):
        button = self.driver.find_element(By.ID, f"add-to-cart-{item_id}")
        self.driver.execute_script("arguments[0].click();", button)

    def get_cart_count(self):
        badges = self.driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
        return badges[0].text if badges else "0"

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    def sort_by(self, option_value):
        dropdown = Select(self.driver.find_element(By.CLASS_NAME, "product_sort_container"))
        dropdown.select_by_value(option_value)

    def get_all_prices(self):
        price_elements = self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        return [float(p.text.replace("$", "")) for p in price_elements]
