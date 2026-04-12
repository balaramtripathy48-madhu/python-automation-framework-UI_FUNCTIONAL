from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def login_internethookup(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("https://the-internet.herokuapp.com/login")
    login_click = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class='radius']")))
    print("login successful")
    login_click.click()

def alert_check_internethookup(driver):
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@onclick='jsAlert()']"))).click()
    alert = driver.switch_to.alert
    print(alert.text)
    alert.accept()

def open_new_window_internethookup(driver):
    driver.get("https://the-internet.herokuapp.com/windows")
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    new_open = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Click Here")))
    new_open.click()
    # time.sleep(2)
    all_windows = driver.window_handles
    driver.switch_to.window(all_windows[1])
    print("window opened successfully")
    assert "new" in driver.current_url, "new window not found"

