from pages.Internethookup_login import InternetHookup
from logging_config import get_logger

logger = get_logger(__name__)

def test_internet_hookup(driver):
    logger.info("Starting InternetHookup login test")
    try:
        login = InternetHookup(driver)
        login.open_url()
        login.enter_username("tomsmith")
        login.enter_password("SuperSecretPassword!")
        login.click_btn()
        logger.info("InternetHookup login completed")

        assert "herokuapp" in driver.current_url
        logger.info("InternetHookup URL verification passed")
    except Exception as e:
        logger.error(f"InternetHookup login test failed: {str(e)}")
        raise
