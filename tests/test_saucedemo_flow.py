import pytest
from pages.saucedemo_flow import *
@pytest.mark.login
def test_saucedemo_flow(driver):
    login_saucedemo(driver,"standard_user","secret_sauce")
    logout_saucedemo(driver)
    assert "Swag Labs" in driver.title, "error message"
    print("logout successful")


@pytest.mark.invalid_login
def test_inavlid_login_1(driver):
    login_saucedemo(driver,"balia","kalia")
    wait = WebDriverWait(driver, 10)
    p = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='error-message-container error']"))).text
    print("user sees error:", p)
    assert "Username and password" in p, "invalid username and password"

