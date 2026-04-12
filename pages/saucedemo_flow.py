from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
def login_saucedemo(driver,username,password):
    driver.implicitly_wait(10)
    driver.get("https://saucedemo.com/")
    search_box= driver.find_element(By.ID,"user-name")
    search_box.send_keys(username)
    search_box_1 = driver.find_element(By.ID,"password")
    search_box_1.send_keys(password)
    sign = driver.find_element(By.ID,"login-button")
    final = sign.click()

def logout_saucedemo(driver):
   wait = WebDriverWait(driver, 10)
   menu = wait.until(EC.presence_of_element_located((By.ID, "react-burger-menu-btn")))
   menu.click()
   log_out = wait.until(EC.presence_of_element_located((By.LINK_TEXT,"Logout")))
   log_out.click()
   # time.sleep(8)
   ti_tle = driver.title
   assert ti_tle == "Swag Labs", "error message"
   print("logout successful")