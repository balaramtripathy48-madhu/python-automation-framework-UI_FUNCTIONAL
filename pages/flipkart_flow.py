from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException
from logging_config import get_logger

logger = get_logger(__name__)

class FlipkartPage:

    def __init__(self, driver):
        logger.debug("Initializing FlipkartPage")
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    # locators
        self.popup = (By.XPATH, "//span[@role='button']")
        self.search_box = (By.NAME, "q")
        self.click_item = (By.PARTIAL_LINK_TEXT,"POCO")
        self.go_cart = (By.XPATH, "//a[@title = 'Cart']")
        self.go_home = (By.XPATH, "//a[contains(@title,'Browse Flipkart categories')]")


    def open_url(self):
        logger.info("Opening Flipkart homepage")
        self.driver.get("https://www.flipkart.com/")
        logger.debug(f"Current URL: {self.driver.current_url}")

    def popup_click(self):
        logger.info("Closing popup")
        try:
            self.wait.until(EC.element_to_be_clickable(self.popup)).click()
            logger.debug("Popup closed successfully")
        except TimeoutException:
            logger.error("Timeout while closing popup")
            raise

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

# def add_to_cart(self):
#     self.wait.until(EC.element_to_be_clickable(self.one_item)).click()
    def click_link(self):
        logger.info("Clicking product link")
        try:
            self.wait.until(EC.element_to_be_clickable(self.click_item)).click()
            logger.debug("Product link clicked successfully")
        except TimeoutException:
            logger.error("Timeout while clicking product link")
            raise

    def switch_to_child(self):
        logger.debug("Switching to child window")
        parent = self.driver.current_window_handle
        for handle in self.driver.window_handles:
            if handle != parent:
                self.driver.switch_to.window(handle)
                logger.debug("Switched to child window successfully")
                break

    def click_go_window(self):
        logger.info("Clicking and switching to product window")
        self.click_link()
        self.switch_to_child()

    def go_to_cart(self):
        logger.info("Navigating to cart")
        for retry in range(6):
            try:
                self.wait.until(EC.element_to_be_clickable(self.go_cart)).click()
                logger.debug("Cart page opened successfully")
                break

            except StaleElementReferenceException:
                logger.warning(f"Stale element reference encountered, retry {retry + 1} of 6")
                if retry == 5:
                    logger.error("Failed to navigate to cart after 6 retries")
                    raise

    def go_home_page(self):
        logger.info("Navigating to home page")
        for retry in range(6):
            try:
                self.wait.until(EC.element_to_be_clickable(self.go_home)).click()
                logger.debug("Home page opened successfully")
                break

            except StaleElementReferenceException:
                logger.warning(f"Stale element reference encountered, retry {retry + 1} of 6")
                if retry == 5:
                    logger.error("Failed to navigate to home page after 6 retries")
                    raise


    def cart_and_home(self):
        logger.info("Starting cart and home navigation sequence")
        self.go_to_cart()
        self.go_home_page()
        logger.debug("Cart and home navigation sequence completed")
