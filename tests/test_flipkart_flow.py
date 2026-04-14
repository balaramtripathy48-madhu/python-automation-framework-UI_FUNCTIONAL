import pytest
from pages.flipkart_flow import flipkart_flow
@pytest.mark.flipkart
@pytest.mark.parametrize("any_search,any_link", [("poco mobiles","POCO C71")])
def test_flipkart_login(driver,any_search,any_link):
    flipkart_flow(driver,any_search,any_link)
    assert "flipkart" in driver.current_url,"inavlid url name"

