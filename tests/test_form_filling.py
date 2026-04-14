from pages.form_filling import filling_form
import pytest
@pytest.mark.filling_form
def test_filling_form(driver):
    filling_form(driver)
    assert "form" in driver.current_url,"form not filled"


from pages.form_filling import filling_form_for_all
@pytest.mark.filling_form
@pytest.mark.parametrize("name,last_name,email,gender,mobile_number,month,year,date,subjects,,hobbies,address,state,city",
        [("soumyaranjan","ghadei","soumyaranjan14@gmail.com","Male","6371857414","January","2002",15,"English","Reading","cuttack,badabajar","Haryana","Karnal")])
def test_form_fill_for_all(driver,name,last_name,email,gender,mobile_number,month,year,date,subjects,hobbies,address,state,city):
    filling_form_for_all(driver,name,last_name,email,gender,mobile_number,month,year,date,subjects,hobbies,address,state,city)
    # time.sleep(5)
    assert "form" in driver.current_url,"form not filled"
