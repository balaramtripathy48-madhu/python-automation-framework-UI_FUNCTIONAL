import pytest
from pages.internethookup_flow import *
from logging_config import get_logger

logger = get_logger(__name__)

@pytest.mark.login
def test_new_login(driver):
    logger.info("Starting InternetHookup login test")
    try:
        login_internethookup(driver)
        logger.info("InternetHookup login completed")
        assert "The Internet"==driver.title
        logger.info("Page title verification passed")
    except Exception as e:
        logger.error(f"Login test failed: {str(e)}")
        raise

@pytest.mark.practice_window
def test_new_window(driver):
    logger.info("Starting new window test")
    try:
        open_new_window_internethookup(driver)
        logger.info("New window test completed")
        assert "internet" in driver.current_url,"invalid url name"
        logger.info("URL verification passed")
    except Exception as e:
        logger.error(f"New window test failed: {str(e)}")
        raise

@pytest.mark.practice_alert
def test_alert_check(driver):
    logger.info("Starting alert check test")
    try:
        alert_check_internethookup(driver)
        logger.info("Alert check test completed")
        logger.info("URL verification passed")
    except Exception as e:
        logger.error(f"Alert check test failed: {str(e)}")
        raise



