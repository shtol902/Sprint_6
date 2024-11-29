import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from data import Url

@pytest.fixture
def driver():
    gecko_service = Service('C:/Users/79174/WebDriver/bin/geckodriver.exe')
    options = Options()
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')
    driver = webdriver.Firefox(service=gecko_service, options=options)
    driver.get(Url.SCOOTER_HOMEPAGE)
    yield driver
    driver.quit()

