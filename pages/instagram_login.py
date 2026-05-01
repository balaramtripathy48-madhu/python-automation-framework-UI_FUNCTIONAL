from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        #locators
        self.username = (By.NAME,"email")
        self.password = (By.NAME,"pass")
        self.logi_btn = (By.XPATH,"//span[text()='Log in']")
    #enter username & password

    def open_url(self):
        self.driver.get("https://www.instagram.com")
    def user_name(self,username):
        self.wait.until((EC.visibility_of_element_located(self.username))).send_keys(username)
    def pass_word(self,password):
        self.wait.until((EC.visibility_of_element_located(self.password))).send_keys(password)
        #click on login
    def login_btn(self):
        self.wait.until((EC.element_to_be_clickable(self.logi_btn))).click()
