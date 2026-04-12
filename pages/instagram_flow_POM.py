from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class login_page:
    def __init__(self,driver):
        self.driver = driver
        #locators
    username = (By.NAME,"email")
    password = (By.NAME,"pass")
    logi_btn = (By.XPATH,"//span[text()='Log in']")
    #enter username & password
    def user_name(self,username):
        wait = WebDriverWait(self.driver, 10)
        wait.until((EC.visibility_of_element_located(*self.username))).send_keys(username)
    def pass_word(self,password):
        wait = WebDriverWait(self.driver, 10)
        wait.until((EC.visibility_of_element_located(*self.password))).send_keys(password)
    def login_btn(self,logi_btn):
        wait = WebDriverWait(self.driver, 10)
        wait.until((EC.element_to_be_clickable(*self.logi_btn))).click()
    def login(self,username,password):
        self.user_name(username)
        self.pass_word(password)
        self.login_btn()
