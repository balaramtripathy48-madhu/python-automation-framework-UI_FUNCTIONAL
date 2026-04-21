from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class InternetHookup:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        # locators
        self.username = (By.NAME, "username")
        self.password = (By.NAME, "password")
        self.login_btn = (By.XPATH, "//button[@class='radius']")

    # Methods
    def open_url(self):
        self.driver.get("https://the-internet.herokuapp.com/login")

    def enter_username(self, username):
        self.wait.until((EC.element_to_be_clickable(self.username))).send_keys(username)

    def enter_password(self, password):
        self.wait.until((EC.element_to_be_clickable(self.password))).send_keys(password)

    def click_btn(self):
        self.wait.until((EC.element_to_be_clickable(self.login_btn))).click()


