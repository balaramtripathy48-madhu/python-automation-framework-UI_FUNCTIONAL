from selenium import webdriver
import time
import selenium.webdriver.support.expected_conditions as EC
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

class AmazonPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    # locators
        self.search_box = (By.ID, "twotabsearchtextbox")
        self.one_item = (By.NAME, "submit.addToCart")
        self.go_cart = (By.ID, "nav-cart")
        self.go_home = (By.ID, "nav-logo-sprites")

    #Actions

    def open_url(self):
        self.driver.get("https://www.amazon.in/ref=nav_logo")

    def enter_search_box(self, search_box):
        items = self.wait.until(EC.element_to_be_clickable(self.search_box))
        items.send_keys(search_box)
        items.send_keys(Keys.ENTER)

    def add_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.one_item)).click()

    def go_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.go_cart)).click()

    def go_home_page(self):
        self.wait.until(EC.element_to_be_clickable(self.go_home)).click()



















