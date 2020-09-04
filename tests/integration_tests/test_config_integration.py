import os
from config import config_dict


class TestConfigIntegrationShould:

    def test_gets_secret_key_from_environment_variables(self):
        for key in config_dict.keys():
            assert config_dict[key].SECRET_KEY == os.environ.get("SIMPYINVOICE_SECRET_KEY")
