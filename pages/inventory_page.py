from selenium.webdriver.common.by import By

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
