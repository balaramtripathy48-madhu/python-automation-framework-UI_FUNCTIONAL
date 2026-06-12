from pages.form_filling import filling_form, filling_form_for_all
import pytest
from logging_config import get_logger

logger = get_logger(__name__)

@pytest.mark.filling_form
def test_filling_form(driver):
    logger.info("Starting form filling test")
    try:
        filling_form(driver)
        logger.info("Basic form filling test completed")
        assert "form" in driver.current_url,"form not filled"
        logger.info("Form URL verification passed")
    except Exception as e:
        logger.error(f"Form filling test failed: {str(e)}")
        raise


@pytest.mark.filling_form
@pytest.mark.parametrize("name,last_name,email,gender,mobile_number,month,year,date,subjects,hobbies,address,state,city",
        [("soumyaranjan","ghadei","soumyaranjan14@gmail.com","Male","6371857414","January","2002",15,"English","Reading","cuttack,badabajar","Haryana","Karnal")])
def test_form_fill_for_all(driver,name,last_name,email,gender,mobile_number,month,year,date,subjects,hobbies,address,state,city):
    logger.info(f"Starting parameterized form filling test for: {name} {last_name}")
    try:
        filling_form_for_all(driver,name,last_name,email,gender,mobile_number,month,year,date,subjects,hobbies,address,state,city)
        logger.info("Parameterized form filling test completed")
        assert "form" in driver.current_url,"form not filled"
        logger.info("Form URL verification passed")
    except Exception as e:
        logger.error(f"Parameterized form filling test failed: {str(e)}")
        raise
