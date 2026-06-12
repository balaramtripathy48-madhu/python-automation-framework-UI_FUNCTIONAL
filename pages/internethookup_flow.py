from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException
from logging_config import get_logger

logger = get_logger(__name__)

def login_internethookup(driver):
    logger.info("Starting InternetHookup login")
    wait = WebDriverWait(driver, 10)
    try:
        driver.get("https://the-internet.herokuapp.com/login")
        logger.debug("Navigated to login page")

        login_click = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@class='radius']")))
        logger.debug("Login button found")
        login_click.click()
        logger.info("Login button clicked")
    except TimeoutException:
        logger.error("Timeout during InternetHookup login")
        raise

def alert_check_internethookup(driver):
    logger.info("Starting alert check for InternetHookup")
    try:
        driver.get("https://the-internet.herokuapp.com/javascript_alerts")
        logger.debug("Navigated to alerts page")

        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@onclick='jsAlert()']"))).click()
        logger.debug("Alert button clicked")

        alert = driver.switch_to.alert
        alert_text = alert.text
        logger.info(f"Alert text detected: {alert_text}")
        alert.accept()
        logger.debug("Alert accepted")
    except TimeoutException:
        logger.error("Timeout during alert check")
        raise
    except Exception as e:
        logger.error(f"Unexpected error during alert check: {str(e)}")
        raise

def open_new_window_internethookup(driver):
    logger.info("Starting new window test for InternetHookup")
    try:
        driver.get("https://the-internet.herokuapp.com/windows")
        logger.debug("Navigated to windows page")

        driver.maximize_window()
        logger.debug("Window maximized")

        wait = WebDriverWait(driver, 10)
        new_open = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Click Here")))
        logger.debug("'Click Here' link found")
        new_open.click()
        logger.debug("'Click Here' link clicked")

        all_windows = driver.window_handles
        logger.debug(f"Total windows open: {len(all_windows)}")
        driver.switch_to.window(all_windows[1])
        logger.info(f"Switched to new window. Current URL: {driver.current_url}")
        any_text = wait.until(EC.visibility_of_element_located((By.XPATH, "//h3[text()='New Window']"))).text
        logger.info(f"Text in new window: {any_text}")
        assert "New Window" in any_text, "Expected text not found in new window"

        # assert "windows" in driver.current_url, "new window not found"
        logger.info("New window opened and verified successfully")
    except TimeoutException:
        logger.error("Timeout during new window test")
        raise
    except AssertionError as e:
        logger.error(f"Assertion failed: {str(e)}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error during new window test: {str(e)}")
        raise
