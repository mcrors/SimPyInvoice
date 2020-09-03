import subprocess
import time
from selenium import webdriver
import pytest


@pytest.fixture()
def firefox_browser():
    options = webdriver.FirefoxOptions()
    # options.add_argument('--headless')
    browser = webdriver.Firefox(options=options)
    yield browser
    browser.quit()


@pytest.fixture(scope='module', autouse=True)
def flask_test_server():
    server = subprocess.Popen(['flask', 'run', '--port', '5000', '--no-reload', '--no-debugger'])
    time.sleep(5)
    yield server
    server.terminate()
