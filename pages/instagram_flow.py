from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def instagram_login(driver,username,password):
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.instagram.com/?hl=en")
    driver.maximize_window()
    wait.until(EC.element_to_be_clickable((By.NAME,"email"))).send_keys(username)
    wait.until(EC.element_to_be_clickable((By.NAME,"pass"))).send_keys(password)
    login_1 = wait.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Log in']")))
    login_1.click()
    not_now = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[text()='Not now']")))
    not_now.click()
    # time.sleep(5)
    not_now_1 = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Not Now']")))
    not_now_1.click()

def instagram_logout(driver):
    wait = WebDriverWait(driver, 10)
    menu = wait.until(EC.element_to_be_clickable((By.XPATH,"//a[@href='/']")))
    menu.click()
    tab_logout = wait.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='More']")))
    tab_logout.click()
    log_out = wait.until(EC.element_to_be_clickable((By.XPATH,"//span[text()='Log out']")))
    log_out.click()
    print("logout successfully")
