from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import sys
import os
path = os.path.dirname(__file__)
sys.path.append(os.path.join(path, "..", ".."))

@pytest.fixture(scope="session")
def setup():
    options = [
        "--start-maximized",
        "--incognito",
        "--disable-gpu",
        "--headless",
        "--disable-extensions",
        "--no-sandbox"
    ]
    chrome_options = Options()
    for option in options:
        chrome_options.add_argument(option)
    driver =  webdriver.Chrome(options=chrome_options)
    yield driver
    sleep(5)
    driver.quit