from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException
from logging_config import get_logger

logger = get_logger(__name__)

def filling_form(driver):
    logger.info("Starting form filling automation")
    wait = WebDriverWait(driver, 40)
    try:
        driver.get("https://demoqa.com/automation-practice-form")
        logger.debug("Navigated to form page")
        
        first_name = wait.until(EC.element_to_be_clickable((By.ID,"firstName")))
        first_name.send_keys("Balaram")
        logger.debug("First name entered: Balaram")
        
        last_name = wait.until(EC.element_to_be_clickable((By.ID,"lastName")))
        last_name.send_keys("Tripathy")
        logger.debug("Last name entered: Tripathy")
        
        email = wait.until(EC.element_to_be_clickable((By.ID,"userEmail")))
        email.send_keys("balaramtripathy48@gmail.com")
        logger.debug("Email entered: balaramtripathy48@gmail.com")
        
        gender = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[@class='form-check form-check-inline']")))
        gender.click()
        logger.debug("Gender selected")
        
        mobile_number = wait.until(EC.element_to_be_clickable((By.ID,"userNumber")))
        mobile_number.send_keys("6372043854")
        logger.debug("Mobile number entered: 6372043854")
        
        dropdown = wait.until(EC.element_to_be_clickable((By.ID,"dateOfBirthInput")))
        dropdown.click()
        logger.debug("Date of birth dropdown opened")
        
        dropdown_selector = Select(wait.until(EC.element_to_be_clickable((By.XPATH,"//select[@class='react-datepicker__month-select']"))))
        dropdown_selector.select_by_visible_text("December")
        logger.debug("Month selected: December")
        
        dropdown_selector_1 = Select(wait.until(EC.visibility_of_element_located((By.XPATH,"//select[@class='react-datepicker__year-select']"))))
        dropdown_selector_1.select_by_visible_text("2002")
        logger.debug("Year selected: 2002")
        
        date = wait.until(EC.element_to_be_clickable((By.XPATH,"//div[contains(@class,'react-datepicker__day react-datepicker__day--022')]")))
        date.click()
        logger.debug("Date selected")
        
        subjects = wait.until(EC.element_to_be_clickable((By.ID,"subjectsInput")))
        subjects.send_keys("Maths")
        subjects.send_keys(Keys.ENTER)
        logger.debug("Subject entered: Maths")
        
        hobbies = wait.until(EC.element_to_be_clickable((By.ID,"hobbies-checkbox-1")))
        hobbies.click()
        logger.debug("Hobby selected")
        
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        address = wait.until(EC.element_to_be_clickable((By.ID,"currentAddress")))
        address.send_keys("bramhana sahi,U.D.S pur")
        logger.debug("Address entered")
        
        dropdown_1 = wait.until(EC.element_to_be_clickable((By.ID,"react-select-3-input")))
        dropdown_1.send_keys("NCR")
        dropdown_1.send_keys(Keys.ENTER)
        logger.debug("State selected: NCR")
        
        dropdown_2 = wait.until(EC.visibility_of_element_located((By.ID,"react-select-4-input")))
        dropdown_2.send_keys("Delhi")
        dropdown_2.send_keys(Keys.ENTER)
        logger.debug("City selected: Delhi")
        
        submit = wait.until(EC.element_to_be_clickable((By.ID,"submit")))
        submit.click()
        logger.info("Form submitted")
        
        final = wait.until(EC.element_to_be_clickable((By.ID,"closeLargeModal")))
        logger.info("Form filled successfully")
        assert final.text == "Close","invalid text"
    except TimeoutException as e:
        logger.error(f"TimeoutException occurred during form filling: {str(e)}")
        raise
    except AssertionError as e:
        logger.error(f"Assertion error: {str(e)}")
        raise

def filling_form_for_all(driver,name,last_name,email,gender,mobile_number,month,year,date,subjects,hobbies,address,state,city):
    logger.info(f"Starting form filling for: {name} {last_name}")
    driver.get("https://demoqa.com/automation-practice-form")
    logger.debug("Navigated to form page")
    
    wait = WebDriverWait(driver,10)
    try:
        nam = wait.until(EC.element_to_be_clickable((By.ID,"firstName")))
        nam.send_keys(name)
        logger.debug(f"First name entered: {name}")
        
        titl = wait.until(EC.element_to_be_clickable((By.ID,"lastName")))
        titl.send_keys(last_name)
        logger.debug(f"Last name entered: {last_name}")
        
        emai = wait.until(EC.element_to_be_clickable((By.ID,"userEmail")))
        emai.send_keys(email)
        logger.debug(f"Email entered: {email}")
        
        wait.until(EC.element_to_be_clickable((By.XPATH,f"//label[text()='{gender}']"))).click()
        logger.debug(f"Gender selected: {gender}")
        
        numb = wait.until(EC.element_to_be_clickable((By.ID,"userNumber")))
        numb.send_keys(mobile_number)
        logger.debug(f"Mobile number entered: {mobile_number}")
        
        wait.until(EC.element_to_be_clickable((By.ID,"dateOfBirthInput"))).click()
        logger.debug("Date of birth dropdown opened")
        
        dropdown = Select(wait.until(EC.visibility_of_element_located((By.XPATH,"//select[@class='react-datepicker__month-select']"))))
        dropdown.select_by_visible_text(month)
        logger.debug(f"Month selected: {month}")
        
        dropdown_1 = Select(wait.until((EC.visibility_of_element_located((By.XPATH,"//select[@class='react-datepicker__year-select']")))))
        dropdown_1.select_by_visible_text(year)
        logger.debug(f"Year selected: {year}")
        
        date_elem = wait.until(EC.visibility_of_element_located((By.XPATH,f"//div[contains(@class,'react-datepicker__day react-datepicker__day--022')]")))
        date_elem.click()
        logger.debug(f"Date selected: {date}")
        
        subject = wait.until(EC.element_to_be_clickable((By.ID,"subjectsInput")))
        subject.send_keys(subjects)
        subject.send_keys(Keys.ENTER)
        logger.debug(f"Subject entered: {subjects}")
        
        hobbies_elem = wait.until(EC.element_to_be_clickable((By.XPATH,f"//label[text()='{hobbies}']")))
        hobbies_elem.click()
        logger.debug(f"Hobby selected: {hobbies}")
        
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        addres = wait.until(EC.element_to_be_clickable((By.ID,"currentAddress")))
        addres.send_keys(address)
        logger.debug(f"Address entered: {address}")
        
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        dropdown_state = wait.until(EC.element_to_be_clickable((By.ID,"react-select-3-input")))
        dropdown_state.send_keys(state)
        dropdown_state.send_keys(Keys.ENTER)
        logger.debug(f"State selected: {state}")
        
        dropdown_city = wait.until(EC.element_to_be_clickable((By.ID,"react-select-4-input")))
        dropdown_city.send_keys(city)
        dropdown_city.send_keys(Keys.ENTER)
        logger.debug(f"City selected: {city}")
        
        submit = wait.until(EC.element_to_be_clickable((By.ID, "submit")))
        driver.execute_script("arguments[0].scrollIntoView();", submit)
        submit.click()
        logger.info("Form submitted")
        
        final = wait.until(EC.element_to_be_clickable((By.ID, "closeLargeModal")))
        logger.info(f"Form filled successfully for: {name} {last_name}")
        assert final.text == "Close", "invalid text"
    except TimeoutException as e:
        logger.error(f"TimeoutException occurred during form filling: {str(e)}")
        raise
    except AssertionError as e:
        logger.error(f"Assertion error: {str(e)}")
        raise
