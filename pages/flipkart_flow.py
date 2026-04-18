from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class FlipkartPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    # locators
        self.popup = (By.XPATH, "//span[@role='button']")
        self.search_box = (By.NAME, "q")
        self.click_item = (By.PARTIAL_LINK_TEXT,"POCO")
        self.go_cart = (By.XPATH, "//a[@title = 'Cart']")
        self.go_home = (By.XPATH, "//a[contains(@title,'Browse Flipkart categories')]")


    def open_url(self):
        self.driver.get("https://www.flipkart.com/")

    def popup_click(self):
        self.wait.until(EC.element_to_be_clickable(self.popup)).click()

    def enter_search_box(self, search_box):
        items = self.wait.until(EC.element_to_be_clickable(self.search_box))
        items.send_keys(search_box)
        items.send_keys(Keys.ENTER)

# def add_to_cart(self):
#     self.wait.until(EC.element_to_be_clickable(self.one_item)).click()
    def click_link(self):
        self.wait.until(EC.element_to_be_clickable(self.click_item)).click()

    def switch_to_child(self):
        parent = self.driver.current_window_handle
        for handle in self.driver.window_handles:
            if handle != parent:
                self.driver.switch_to.window(handle)
                break

    def click_go_window(self):
        self.click_link()
        self.switch_to_child()

    def go_to_cart(self):
        for retry in range(6):
            try:
                self.wait.until(EC.element_to_be_clickable(self.go_cart)).click()
                break

            except StaleElementReferenceException:
                if retry == 5:
                    raise

    def go_home_page(self):
        for retry in range(6):
            try:
                self.wait.until(EC.element_to_be_clickable(self.go_home)).click()
                break

            except StaleElementReferenceException:
                if retry == 5:
                    raise


    def cart_and_home(self):
        self.go_to_cart()
        self.go_home_page()






