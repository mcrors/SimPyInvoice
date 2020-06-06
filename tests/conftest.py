import pytest
from simpyinvoice import create_app


# @pytest.fixture(scope='session')
# def add_app_to_sys_path():
#     currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
#     parentdir = os.path.dirname(currentdir)
#     app_dir = os.path.join(parentdir, "simpyinvoice")
#     if app_dir not in os.sys.path:
#         os.sys.path.extend([app_dir])


@pytest.fixture()
def client():
    app = create_app('test')
    testing_client = app.test_client()
    app_cntxt = app.app_context()
    app_cntxt.push()
    yield testing_client
    app_cntxt.pop()
