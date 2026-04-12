import pytest
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.internethookup_flow import login_internethookup
from pages.saucedemo_flow import login_saucedemo
from pages.flipkart_flow import flipkart_flow

@pytest.mark.login
def test_new_login(driver):
    login_internethookup(driver)
    # time.sleep(5)
    assert "The Internet"==driver.title

@pytest.mark.flipkart
@pytest.mark.parametrize("any_search,any_link", [("poco mobiles","POCO C71")])
def test_flipkart_login(driver,any_search,any_link):
    flipkart_flow(driver,any_search,any_link)
    assert "Cart" in driver.title


@pytest.mark.login
def test_inavlid_login_1(driver):
    login_saucedemo(driver,"balia","kalia")
    wait = WebDriverWait(driver, 10)
    p = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='error-message-container error']"))).text
    print("user sees error:", p)
    assert "Username and password" in p, "invalid username and password"

