from pages.Internethookup_login import InternetHookup
def test_internet_hookup(driver):
    login = InternetHookup(driver)
    login.open_url()
    login.enter_username("tomsmith")
    login.enter_password("SuperSecretPassword!")
    login.click_btn()
    assert "herokuapp" in driver.current_url