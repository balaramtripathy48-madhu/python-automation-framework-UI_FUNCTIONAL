import pytest
from pages.flipkart_flow import FlipkartPage
@pytest.mark.flipkart
@pytest.mark.parametrize("search_box",["POCO C71"])
def test_flipkart_flow(driver,search_box):
    flow = FlipkartPage(driver)
    flow.open_url()
    flow.popup_click()
    flow.enter_search_box(search_box)
    flow.click_go_window()
    flow.cart_and_home()
    assert "flipkart" in driver.current_url,"inavlid url name"

