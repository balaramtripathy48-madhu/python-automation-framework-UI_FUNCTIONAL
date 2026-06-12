from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common import TimeoutException
from logging_config import get_logger

logger = get_logger(__name__)

class InternetHookup:
    def __init__(self, driver):
        logger.debug("Initializing InternetHookup")
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        # locators
        self.username = (By.NAME, "username")
        self.password = (By.NAME, "password")
        self.login_btn = (By.XPATH, "//button[@class='radius']")

    # Methods
    def open_url(self):
        logger.info("Opening InternetHookup login page")
        self.driver.get("https://the-internet.herokuapp.com/login")
        logger.debug(f"Current URL: {self.driver.current_url}")

    def enter_username(self, username):
        logger.info(f"Entering username: {username}")
        try:
            self.wait.until((EC.element_to_be_clickable(self.username))).send_keys(username)
            logger.debug("Username entered successfully")
        except TimeoutException:
            logger.error("Timeout while entering username")
            raise

    def enter_password(self, password):
        logger.info("Entering password")
        try:
            self.wait.until((EC.element_to_be_clickable(self.password))).send_keys(password)
            logger.debug("Password entered successfully")
        except TimeoutException:
            logger.error("Timeout while entering password")
            raise
        #click login btn

    def click_btn(self):
        logger.info("Clicking login button")
        try:
            self.wait.until((EC.element_to_be_clickable(self.login_btn))).click()
            logger.info("Login successful")
        except TimeoutException:
            logger.error("Timeout while clicking login button")
            raise
