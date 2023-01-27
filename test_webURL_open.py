# Parallel testing using cmd pytest -n 4
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


@pytest.mark.usefixtures("timespan")
class TestLaunchURLs:
    def test_google(self, timespan):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.implicitly_wait(10)
        driver.get("https://www.google.com")
        assert driver.title=="Google"
        driver.quit()

    def test_facebook(self, timespan):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.implicitly_wait(10)
        driver.get("https://www.facebook.com")
        assert driver.title=='Facebook – log in or sign up'
        driver.quit()

    def test_insta(self, timespan):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.implicitly_wait(10)
        driver.get("https://www.instagram.com")
        assert driver.title=="Instagram"
        driver.quit()

    def test_gmail(self, timespan):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.implicitly_wait(10)
        driver.get("https://www.gmail.com")
        assert driver.title=="Gmail"
        driver.quit()

    def test_rediff(self, timespan):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.implicitly_wait(10)
        driver.get("https://www.rediff.com")
        assert driver.title=="Rediff.com"
        driver.quit()