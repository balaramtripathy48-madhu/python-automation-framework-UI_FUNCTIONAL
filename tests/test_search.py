import pytest
from pages.youtube_flow import youtube_search
from logging_config import get_logger

logger = get_logger(__name__)

@pytest.mark.youtube
@pytest.mark.parametrize("search_song,exact_song", [("dhruv rathee","Every LIE in Dhurandhar 2 EXPOSED | Dhruv Rathee"),("ashish chanchlani","ASHISH CHANCHLANI VINES : THE DEVDAS DUB")])
def test_youtube_song(driver,search_song,exact_song):
    logger.info(f"Starting YouTube search test for: {search_song}")
    try:
        youtube_search(driver,search_song,exact_song)
        logger.debug(f"Taking screenshot for: {search_song}")
        driver.save_screenshot(f"reports/{search_song}.png")
        logger.debug(f"Screenshot saved for: {search_song}")

        assert "watch?v" in driver.current_url
        logger.info(f"YouTube search test completed successfully for: {search_song}")
    except Exception as e:
        logger.error(f"YouTube search test failed for {search_song}: {str(e)}")
        raise
