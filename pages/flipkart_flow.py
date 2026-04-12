from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def flipkart_flow(driver,any_search,any_link):
    driver.get("https://www.flipkart.com/")
    wait = WebDriverWait(driver, 10)
    driver.maximize_window()
    popup = wait.until(EC.element_to_be_clickable((By.XPATH,"//span[@role='button']")))
    popup.click()
    search_box = wait.until(EC.element_to_be_clickable((By.NAME,"q")))
    search_box.send_keys(any_search)
    search_box.send_keys(Keys.ENTER)
    # time.sleep(5)
    exact_mobile = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT,any_link)))
    exact_mobile.click()
    current_window = driver.current_window_handle
    all_windows = driver.window_handles
    for handle in all_windows:
        if handle != current_window:
            driver.switch_to.window(handle)
    # time.sleep(5)
    # click_cart = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='css-g5y9jx']")))
    # click_cart.click()
    # go_cart = wait.until(EC.element_to_be_clickable((By.XPATH,"//a[@title='Cart']")))
    # go_cart.click()

