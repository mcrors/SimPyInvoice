import pytest
from config import config_dict, Configuration, ProdConfiguration, TestConfiguration, DevConfiguration


class TestConfigShould:

    @staticmethod
    def test_config_dict_contains_4_entries():
        assert len(config_dict) == 4

    @staticmethod
    def test_config_dict_items_are_of_type_config():
        for value in config_dict.values():
            assert issubclass(value, Configuration)

    @staticmethod
    @pytest.mark.parametrize("key, result", [
        ("prod", ProdConfiguration),
        ("test", TestConfiguration),
        ("dev", DevConfiguration),
        ("default", DevConfiguration)
    ])
    def test_config_values_are_correct_sub_type(key, result):
        assert issubclass(config_dict[key], result)

    @staticmethod
    def test_config_contains_secret_key():
        for key in config_dict.keys():
            assert hasattr(config_dict[key], "SECRET_KEY")

    @staticmethod
    def test_that_test_configurtaion_testing_attr_is_true():
        test_config = TestConfiguration()
        assert test_config.TESTING is True

    @staticmethod
    @pytest.mark.parametrize('env', [
        'prod',
        'test',
        'dev'
    ])
    def test_database_uri_is_set_for_all_envs(env):
        config_class = config_dict[env]
        assert 'SQLALCHEMY_DATABASE_URI' in config_class.__dict__.keys()
