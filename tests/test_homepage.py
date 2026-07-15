from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_homepage_title():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com")

    assert "Swag Labs" in driver.title

    time.sleep(2)
    driver.quit()