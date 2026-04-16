import pytest
from pages.instagram_login import  loginPage
from pages.instagram_logout import instagram_logout
@pytest.mark.parametrize("username,password",[("balaramtripathy48@gmail.com","Balia@2001")])
def test_insta_login(driver,username,password):
    login = loginPage(driver)
    login.open_url()
    login.user_name(username)
    login.pass_word(password)
    login.login_btn()
    instagram_logout(driver)
    assert "instagram" in driver.current_url ,"invalid url"
