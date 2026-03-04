import json
import os


class ConfigReader:

    def __init__(self):
        config_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "config",
            "config.json"
        )

        with open(config_path) as config_file:
            self.config = json.load(config_file)

    def get(self, key):
        return self.config.get(key)