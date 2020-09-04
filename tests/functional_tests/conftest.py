from pathlib import Path
import subprocess
import time
from selenium import webdriver
import pytest
import docker


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

