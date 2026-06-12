import pytest
from pages.flipkart_flow import FlipkartPage
from logging_config import get_logger

logger = get_logger(__name__)

@pytest.mark.flipkart
@pytest.mark.parametrize("search_box",["POCO C71"])
def test_flipkart_flow(driver,search_box):
    logger.info(f"Starting Flipkart flow test for product: {search_box}")
    try:
        flow = FlipkartPage(driver)
        flow.open_url()
        flow.popup_click()
        flow.enter_search_box(search_box)
        flow.click_go_window()
        flow.cart_and_home()
        logger.info(f"Flipkart flow completed successfully for product: {search_box}")

        assert "flipkart" in driver.current_url,"inavlid url name"
        logger.info("URL verification passed for Flipkart")
    except Exception as e:
        logger.error(f"Test failed for product {search_box}: {str(e)}")
        raise

