import pytest
from pages.youtube_flow import youtube_search
@pytest.mark.youtube
@pytest.mark.parametrize("search_song,exact_song", [("dhruv rathee","Every LIE in Dhurandhar 2 EXPOSED | Dhruv Rathee"),("ashish chanchlani","”I got FIRs for laughing at someone else's joke (India’s Got Latent)….” - Ashish Chanchlani | #169")])
def test_youtube_song(driver,search_song,exact_song):
    youtube_search(driver,search_song,exact_song)
    driver.save_screenshot(f"reports/{search_song}.png")
    assert "watch?v" in driver.current_url

