import pytest
from app.models import User


class TestUserShould:

    @staticmethod
    def test_password_setter():
        user = User(password='cat')
        assert user.password_hash is not None

    @staticmethod
    def test_no_password_getter():
        user = User(password='cat')
        with pytest.raises(AttributeError):
            user.password

    @staticmethod
    def test_password_verification():
        user = User(password='cat')
        assert user.verify_password('cat') is True
        assert user.verify_password('dog') is False

    @staticmethod
    def test_password_salts_are_random():
        user1 = User(password='cat')
        user2 = User(password='cat')
        assert user1.password_hash != user2.password_hash
