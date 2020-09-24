from pathlib import Path
import time
from selenium import webdriver
import pytest
import docker

from tests.functional_tests.func_test_utils import register_via_browser, login_via_browser


@pytest.fixture()
def firefox_browser():
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')
    browser = webdriver.Firefox(options=options)
    yield browser
    browser.quit()


@pytest.fixture()
def simpy_test_container(app_dir):
    docker_context = str(Path(app_dir).parent)
    docker_client = docker.from_env()
    docker_client.images.build(path=docker_context,
                               rm=True,
                               tag='simpyinvoice:test',
                               dockerfile='Dockerfile.test')
    container = docker_client.containers.run('simpyinvoice:test',
                                             name='simpyinvoice',
                                             detach=True,
                                             ports={'5000': '5000'})
    time.sleep(5)
    yield
    container.kill()
    container.remove()


@pytest.fixture()
def register_and_login(firefox_browser, simpy_test_container):
    arthur = {
        'first_name': 'Arthur',
        'last_name': 'Camalot',
        'username': 'arthur',
        'email': 'arthur@camalot.com',
        'password': '123456789'
    }
    register_via_browser(firefox_browser,
                         arthur['first_name'],
                         arthur['last_name'],
                         arthur['username'],
                         arthur['email'],
                         arthur['password'])
    login_via_browser(firefox_browser, arthur['email'], arthur['password'])
    yield
