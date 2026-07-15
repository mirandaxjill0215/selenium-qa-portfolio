from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_valid_login():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(1)
    assert "inventory" in driver.current_url

    driver.quit()

def test_invalid_login():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com")

    driver.find_element(By.ID, "user-name").send_keys("wrong_user")
    driver.find_element(By.ID, "password").send_keys("wrong_password")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(1)
    error = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
    assert "Username and password do not match" in error.text

    driver.quit()


def test_empty_fields_login():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com")

    driver.find_element(By.ID, "login-button").click()

    time.sleep(1)
    error = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
    assert "Username is required" in error.text

    driver.quit()