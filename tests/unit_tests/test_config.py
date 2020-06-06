import pytest
from config import config_dict, Configuration, ProdConfiguration, TestConfiguration, DevConfiguration


class TestConfigShould:

    def test_config_dict_contains_4_entries(self):
        assert len(config_dict) == 4

    def test_config_dict_items_are_of_type_config(self):
        for value in config_dict.values():
            assert issubclass(value, Configuration)

    @pytest.mark.parametrize("key, result", [
        ("prod", ProdConfiguration),
        ("test", TestConfiguration),
        ("dev", DevConfiguration),
        ("default", DevConfiguration)
    ])
    def test_config_values_are_correct_sub_type(self, key, result):
        assert issubclass(config_dict[key], result)

    def test_config_contains_secret_key(self):
        for key in config_dict.keys():
            assert hasattr(config_dict[key], "SECRET_KEY")

    def test_that_test_configurtaion_testing_attr_is_true(self):
        test_config = TestConfiguration()
        assert test_config.TESTING is True
