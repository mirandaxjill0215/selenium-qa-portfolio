from driver_factory import get_driver
import time

def test_homepage_title():
    driver = get_driver()
    driver.get("https://www.saucedemo.com")

    assert "Swag Labs" in driver.title

    time.sleep(2)
    driver.quit()
