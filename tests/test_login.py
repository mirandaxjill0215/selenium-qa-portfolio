from selenium import webdriver
from pages.login_page import LoginPage
import time

def test_valid_login():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    time.sleep(1)
    assert "inventory" in driver.current_url

    driver.quit()


def test_invalid_login():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("wrong_user", "wrong_password")

    time.sleep(1)
    assert "Username and password do not match" in login_page.get_error_message()

    driver.quit()


def test_empty_fields_login():
    driver = webdriver.Chrome()
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("", "")

    time.sleep(1)
    assert "Username is required" in login_page.get_error_message()

    driver.quit()