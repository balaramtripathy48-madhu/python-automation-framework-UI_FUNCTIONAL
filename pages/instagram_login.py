from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException
from logging_config import get_logger

logger = get_logger(__name__)

class LoginPage:
    def __init__(self,driver):
        logger.debug("Initializing LoginPage")
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        #locators
        self.username = (By.NAME,"email")
        self.password = (By.NAME,"pass")
        self.logi_btn = (By.XPATH,"//span[text()='Log in']")
    #enter username & password

    def open_url(self):
        logger.info("Opening Instagram login page")
        self.driver.get("https://www.instagram.com")
        logger.debug(f"Current URL: {self.driver.current_url}")

    def user_name(self,username):
        logger.info(f"Entering username: {username}")
        try:
            self.wait.until((EC.visibility_of_element_located(self.username))).send_keys(username)
            logger.debug("Username entered successfully")
        except TimeoutException:
            logger.error("Timeout while entering username")
            raise

    def pass_word(self,password):
        logger.info("Entering password")
        try:
            self.wait.until((EC.visibility_of_element_located(self.password))).send_keys(password)
            logger.debug("Password entered successfully")
        except TimeoutException:
            logger.error("Timeout while entering password")
            raise
        #click on login

    def login_btn(self):
        logger.info("Clicking login button")
        try:
            self.wait.until((EC.element_to_be_clickable(self.logi_btn))).click()
            logger.debug("Login button clicked successfully")
        except TimeoutException:
            logger.error("Timeout while clicking login button")
            raise
