import os
import inspect
import pytest
from app import create_app
from app.models import User


@pytest.fixture()
def a_test_user():
    return {
        'email': 'sir.lancelot@camolot.com',
        'username': 'sir_lancelot',
        'first_name': 'lancelot',
        'last_name': 'camolot',
        'password': 'blue!,no!yellow!'
    }


@pytest.fixture()
def app_dir():
    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    parentdir = os.path.dirname(currentdir)
    flask_app_dir = os.path.join(parentdir, "app")
    return flask_app_dir


@pytest.fixture(scope='session')
def app():
    from app import db
    simpy_invoice_app = create_app('test')
    app_cntxt = simpy_invoice_app.app_context()
    app_cntxt.push()
    db.create_all()
    yield simpy_invoice_app
    db.session.remove()
    db.drop_all()
    app_cntxt.pop()


@pytest.fixture()
def simpyinvoice_client():
    from app import db
    simpy_invoice_app = create_app('test')
    testing_client = simpy_invoice_app.test_client(use_cookies=True)
    app_cntxt = simpy_invoice_app.app_context()
    app_cntxt.push()
    db.create_all()
    yield testing_client
    db.session.remove()
    db.drop_all()
    app_cntxt.pop()


@pytest.fixture()
def db_with_one_user(app, a_test_user):
    from app import db
    user = User(email=a_test_user['email'],
                username=a_test_user['username'],
                first_name=a_test_user['first_name'],
                last_name=a_test_user['last_name'])
    user.password = a_test_user['password']
    db.session.add(user)
    db.session.commit()
    return db


@pytest.fixture()
def logged_in_user(simpyinvoice_client, db_with_one_user, a_test_user):
    simpyinvoice_client.post('/auth/login', data={
        'email': a_test_user['email'],
        'password': a_test_user['password']
    })
    yield
