from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException
from logging_config import get_logger

logger = get_logger(__name__)

def youtube_search(driver, search_song, exact_song):
    logger.info(f"Starting YouTube search for: {search_song}")
    wait = WebDriverWait(driver, 10)
    try:
        driver.get("https://www.youtube.com/")
        logger.debug("Navigated to YouTube homepage")
        
        search_box = wait.until(EC.element_to_be_clickable((By.NAME, "search_query")))
        logger.debug("Search box found")
        
        search_box.send_keys(search_song)
        logger.debug(f"Entered search query: {search_song}")
        
        search_box.send_keys(Keys.ENTER)
        logger.debug("Search submitted")
        
        song_1 = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, f"{exact_song}")))
        logger.debug(f"Found song link: {exact_song}")
        
        song_1.click()
        logger.info(f"Clicked on song: {exact_song}")
    except TimeoutException:
        logger.error(f"Timeout during YouTube search for: {search_song}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error during YouTube search: {str(e)}")
        raise
