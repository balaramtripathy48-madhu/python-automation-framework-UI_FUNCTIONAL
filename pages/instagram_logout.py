from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class InstagramFlow:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)
    #locators
        self.menu = (By.XPATH,"//a[@href='/']")
        self.more = (By.XPATH,"//span[text()='More']")
        self.logout = (By.XPATH,"//span[text()='Log out']")

    #Methods
    def menu_option(self):
        self.wait.until(EC.element_to_be_clickable(self.menu)).click()

    def more_option(self):
        self.wait.until(EC.element_to_be_clickable(self.more)).click()

    def logout_option(self):
        self.wait.until(EC.element_to_be_clickable(self.logout)).click()
        print("logout successfully")

