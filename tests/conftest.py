import os
import inspect
import pytest


@pytest.fixture(scope='session')
def add_app_to_sys_path():
    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    parentdir = os.path.dirname(currentdir)
    app_dir = os.join(parentdir, "simpyinvoice")
    if app_dir not in os.sys.path:
        os.sys.path.extend([app_dir])
