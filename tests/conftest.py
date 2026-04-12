import pytest
import time
from selenium import webdriver
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def my_input():
    x = (5,6)
    return x

@pytest.fixture
def insta_login(driver):
    driver=driver
    driver.get("https://www.instagram.com/?hl=en")
    wait = WebDriverWait(driver,10)
    driver.maximize_window()
    wait.until(EC.element_to_be_clickable((By.NAME, "email"))).send_keys("balaramtripathy48@gmail.com")
    wait.until(EC.element_to_be_clickable((By.NAME, "pass"))).send_keys("Balia@2001")
    login_1 = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Log in']")))
    login_1.click()
    not_now = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Not now']")))
    not_now.click()
    not_now_1 = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Not Now']")))
    not_now_1.click()
