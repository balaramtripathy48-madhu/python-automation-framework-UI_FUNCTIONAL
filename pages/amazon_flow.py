from selenium import webdriver
import time
import selenium.webdriver.support.expected_conditions as EC
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
def open_amazon(driver):
    driver.get("https://www.amazon.in/")
    driver.maximize_window()
def search_box(driver,any_item):
    wait = WebDriverWait(driver, 10)
    search = wait.until(EC.element_to_be_clickable((By.ID,"twotabsearchtextbox")))
    search.send_keys(any_item)
    search.send_keys(Keys.ENTER)
def add_to_cart(driver):
    wait = WebDriverWait(driver, 10)
    select = wait.until(EC.element_to_be_clickable((By.NAME,"submit.addToCart")))
    select.click()
    time.sleep(5)
def go_to_cart(driver):
    wait = WebDriverWait(driver, 10)
    select = wait.until(EC.element_to_be_clickable((By.ID,"nav-cart-count-container")))
    select.click()
def go_to_home(driver):
    wait = WebDriverWait(driver, 10)
    select = wait.until(EC.element_to_be_clickable((By.ID,"nav-logo-sprites")))
    select.click()
















