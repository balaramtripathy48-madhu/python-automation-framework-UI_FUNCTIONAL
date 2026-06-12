import pytest
from pages.amazon_flow import AmazonPage
from logging_config import get_logger

logger = get_logger(__name__)

@pytest.mark.amazon
@pytest.mark.parametrize("any_item",["mobiles","led tv"])
def test_amazon_flow(driver,any_item):
    logger.info(f"Starting Amazon full flow test for item: {any_item}")
    try:
        flow = AmazonPage(driver)
        flow.open_url()
        flow.enter_search_box(any_item)
        flow.add_to_cart()
        flow.go_to_cart()
        flow.go_home_page()
        logger.info(f"Amazon flow completed successfully for item: {any_item}")
        
        assert "amazon" in driver.current_url, "check the url"
        logger.info("URL verification passed for Amazon")
    except Exception as e:
        logger.error(f"Test failed for item {any_item}: {str(e)}")
        raise
