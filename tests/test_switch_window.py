import pytest
from pages.internethookup_flow import open_new_window_internethookup
@pytest.mark.practice_window
def test_new_window(driver):
    open_new_window_internethookup(driver)