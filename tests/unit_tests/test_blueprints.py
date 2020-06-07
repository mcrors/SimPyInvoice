from flask import Blueprint
import pytest
from app import create_app
from app.main import main
from app.auth import auth


class TestBlueprintsShould:

    def test_blueprints_exist(self):
        assert isinstance(main, Blueprint)
        assert isinstance(auth, Blueprint)

    @pytest.mark.parametrize("blueprint_instance", [
        ("main"),
        ("auth")
    ])
    def test_main_blueprint_is_registered(self, blueprint_instance):
        app = create_app("test")
        blueprint = app.blueprints[blueprint_instance]
        assert blueprint
