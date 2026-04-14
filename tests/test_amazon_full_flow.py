import pytest
from amazon_flow import *
@pytest.mark.amazon
@pytest.mark.parametrize("any_item",["mobiles","led tv"])
def test_amazon_flow(driver,any_item):
        open_amazon(driver)
        search_box(driver,any_item)
        time.sleep(5)
        add_to_cart(driver)
        go_to_cart(driver)
        driver.save_screenshot(f"reports/{any_item}.png")
        assert "cart" in driver.current_url, "cart in url"
        go_to_home(driver)
        print("home page opened successfully")
        assert "amazon" in driver.current_url, "check the url"