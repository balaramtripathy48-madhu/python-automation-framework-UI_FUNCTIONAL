import pytest
from pages.amazon_flow import AmazonPage
@pytest.mark.amazon
@pytest.mark.parametrize("any_item",["mobiles","led tv"])
def test_amazon_flow(driver,any_item):
        flow = AmazonPage(driver)
        flow.open_url()
        flow.enter_search_box(any_item)
        flow.add_to_cart()
        flow.go_to_cart()
        flow.go_home_page()
        print("home page opened successfully")
        assert "amazon" in driver.current_url, "check the url"