from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def get_cart_items(self):
        return self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")

    def get_item_names(self):
        return [item.text for item in self.get_cart_items()]