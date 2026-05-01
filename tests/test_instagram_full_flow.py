import pytest
from pages.instagram_logout import InstagramFlow
from pages.instagram_login import LoginPage
@pytest.mark.parametrize("username,password",[("balaramtripathy48@gmail.com","Balia@2001")])
def test_insta(driver,username,password):
    login = LoginPage(driver)
    flow = InstagramFlow(driver)
    login.open_url()
    login.user_name("balaramtripathy48@gmail.com")
    login.pass_word("Balia@2001")
    login.login_btn()
    flow.menu_option()
    flow.more_option()
    flow.logout_option()
    assert "instagram" in driver.current_url ,"invalid url"

