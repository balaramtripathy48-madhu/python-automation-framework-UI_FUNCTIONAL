import pytest
from pages.instagram_logout import InstagramFlow
from pages.instagram_login import LoginPage
from logging_config import get_logger

logger = get_logger(__name__)

@pytest.mark.parametrize("username,password",[("balaramtripathy48@gmail.com","Balia@2001")])
def test_insta(driver,username,password):
    logger.info(f"Starting Instagram login flow test with username: {username}")
    try:
        login = LoginPage(driver)
        flow = InstagramFlow(driver)

        login.open_url()
        login.user_name("balaramtripathy48@gmail.com")
        login.pass_word("Balia@2001")
        login.login_btn()
        logger.info("Instagram login successful")

        flow.menu_option()
        flow.more_option()
        flow.logout_option()
        logger.info("Instagram logout flow completed successfully")

        assert "instagram" in driver.current_url ,"invalid url"
        logger.info("Instagram URL verification passed")
    except Exception as e:
        logger.error(f"Instagram flow test failed: {str(e)}")
        raise

