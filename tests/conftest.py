import os
import inspect
import pytest
from app import create_app, db
from app.models import User


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
    db.create_all()
    yield app
    db.session.remove()
    db.drop_all()
    app_cntxt.pop()


@pytest.fixture()
def client():
    app = create_app('test')
    testing_client = app.test_client()
    app_cntxt = app.app_context()
    app_cntxt.push()
    db.create_all()
    yield testing_client
    db.session.remove()
    db.drop_all()
    app_cntxt.pop()


@pytest.fixture()
def db_with_one_user(simpyinvoice_app):
    user = User(email='sir.lancelot@camolot.com',
                username='sir_lancelot',
                first_name='lancelot',
                last_name='camolot')
    user.password = 'blue_no_yellow'
    db.session.add(user)
    db.session.commit()
    return db
