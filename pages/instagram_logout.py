from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException
from logging_config import get_logger

logger = get_logger(__name__)

class InstagramFlow:
    def __init__(self,driver):
        logger.debug("Initializing InstagramFlow")
        self.driver = driver
        self.wait = WebDriverWait(driver,10)
    #locators
        self.menu = (By.XPATH,"//a[@href='/']")
        self.more = (By.XPATH,"//span[text()='More']")
        self.logout = (By.XPATH,"//span[text()='Log out']")

    #Methods
    def menu_option(self):
        logger.info("Clicking menu option")
        try:
            self.wait.until(EC.element_to_be_clickable(self.menu)).click()
            logger.debug("Menu option clicked successfully")
        except TimeoutException:
            logger.error("Timeout while clicking menu option")
            raise

    def more_option(self):
        logger.info("Clicking 'More' option")
        try:
            self.wait.until(EC.element_to_be_clickable(self.more)).click()
            logger.debug("'More' option clicked successfully")
        except TimeoutException:
            logger.error("Timeout while clicking 'More' option")
            raise

    def logout_option(self):
        logger.info("Clicking logout option")
        try:
            self.wait.until(EC.element_to_be_clickable(self.logout)).click()
            logger.info("Logout successful")
        except TimeoutException:
            logger.error("Timeout while clicking logout option")
            raise

