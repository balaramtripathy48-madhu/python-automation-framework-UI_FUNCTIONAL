import pytest
from pages.internethookup_flow import *
@pytest.mark.login
def test_new_login(driver):
    login_internethookup(driver)
    # time.sleep(5)
    assert "The Internet"==driver.title

@pytest.mark.practice_window
def test_new_window(driver):
    open_new_window_internethookup(driver)
    assert "internet" in driver.current_url,"invalid url name"

@pytest.mark.practice_alert
def test_alert_check(driver):
    alert_check_internethookup(driver)
    assert "windows" in driver.current_url,"invalid url name"



