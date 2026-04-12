import pytest
from pages.instagram_flow import *
@pytest.mark.instagram
def test_insta_loin_logout(driver,insta_login):
    instagram_logout(driver)
    assert "instagram" in driver.current_url ,"invalid url"
