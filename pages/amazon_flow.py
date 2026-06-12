from selenium import webdriver
import time
import selenium.webdriver.support.expected_conditions as EC
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from logging_config import get_logger

logger = get_logger(__name__)

class AmazonPage:

    def __init__(self, driver):
        logger.debug("Initializing AmazonPage")
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    # locators
        self.search_box = (By.ID, "twotabsearchtextbox")
        self.one_item = (By.NAME, "submit.addToCart")
        self.go_cart = (By.ID, "nav-cart")
        self.go_home = (By.ID, "nav-logo-sprites")

    #Actions

    def open_url(self):
        logger.info("Opening Amazon.in homepage")
        self.driver.get("https://www.amazon.in/ref=nav_logo")
        logger.debug(f"Current URL: {self.driver.current_url}")

    def enter_search_box(self, search_box):
        logger.info(f"Searching for item: {search_box}")
        try:
            items = self.wait.until(EC.element_to_be_clickable(self.search_box))
            items.send_keys(search_box)
            items.send_keys(Keys.ENTER)
            logger.debug(f"Search completed for: {search_box}")
        except TimeoutException:
            logger.error(f"Timeout while searching for item: {search_box}")
            raise

    def add_to_cart(self):
        logger.info("Adding item to cart")
        try:
            self.wait.until(EC.element_to_be_clickable(self.one_item)).click()
            logger.debug("Item added to cart successfully")
        except TimeoutException:
            logger.error("Timeout while adding item to cart")
            raise

    def go_to_cart(self):
        logger.info("Navigating to cart")
        try:
            self.wait.until(EC.element_to_be_clickable(self.go_cart)).click()
            logger.debug("Cart page opened successfully")
        except TimeoutException:
            logger.error("Timeout while navigating to cart")
            raise

    def go_home_page(self):
        logger.info("Navigating to home page")
        try:
            self.wait.until(EC.element_to_be_clickable(self.go_home)).click()
            logger.debug("Home page opened successfully")
        except TimeoutException:
            logger.error("Timeout while navigating to home page")
            raise



















