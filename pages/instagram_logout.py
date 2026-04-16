from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def instagram_logout(driver):
    wait = WebDriverWait(driver, 10)
    menu = wait.until(EC.element_to_be_clickable((By.XPATH,"//a[@href='/']")))
    menu.click()
    tab_logout = wait.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='More']")))
    tab_logout.click()
    log_out = wait.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Log out']")))
    log_out.click()
    print("logout successfully")
