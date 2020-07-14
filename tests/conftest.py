import os
import inspect
import pytest
from app import create_app


@pytest.fixture(scope='session')
def app_dir():
    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    parentdir = os.path.dirname(currentdir)
    flask_app_dir = os.path.join(parentdir, "app")
    return flask_app_dir


@pytest.fixture()
def simpyinvoice_app():
    app = create_app('test')
    app_cntxt = app.app_context()
    app_cntxt.push()
    yield app
    app_cntxt.pop()


@pytest.fixture()
def client():
    app = create_app('test')
    testing_client = app.test_client()
    app_cntxt = app.app_context()
    app_cntxt.push()
    yield testing_client
    app_cntxt.pop()
