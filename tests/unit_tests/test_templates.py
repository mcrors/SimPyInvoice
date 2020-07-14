import os
import pathlib
import pytest


@pytest.fixture()
def templates_dir(app_dir):
    app_parent = pathlib.Path(app_dir).parent
    return pathlib.Path(os.path.join(app_parent, 'templates'))


class TestTemplatesShould:

    @staticmethod
    @pytest.mark.parametrize('page', [
        'home.html',
        'base.html'
    ])
    def test_templates_contains_html_files(templates_dir, page):
        assert templates_dir.is_dir()
        page_under_test = os.path.join(templates_dir, page)
        assert os.path.exists(page_under_test), f'{page} not found'

    @staticmethod
    def test_all_templates_use_base_html(templates_dir):
        expected_text = '{% extends "base.html" %}'
        for file in templates_dir.iterdir():
            if file.name != 'base.html':
                with open(file, 'r') as f:
                    contents = f.read()
                    assert expected_text in contents, f'base.html not in file {file}'
