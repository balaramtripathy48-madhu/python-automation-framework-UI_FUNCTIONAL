from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def youtube_search(driver, search_song, exact_song):
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.youtube.com/")
    driver.maximize_window()
    search_box = wait.until(EC.element_to_be_clickable((By.NAME, "search_query")))
    search_box.send_keys(search_song)
    search_box.send_keys(Keys.ENTER)
    song_1 = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, f"{exact_song}")))
    song_1.click()