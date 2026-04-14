import pytest
from pages.instagram_flow import *
@pytest.mark.parametrize("username,password",[("balaramtripathy48@gmail.com","Balia@2001")])
def test_insta_login_logout(driver,username,password):
    instagram_login(driver, username, password)
    instagram_logout(driver)
    assert "instagram" in driver.current_url ,"invalid url"
