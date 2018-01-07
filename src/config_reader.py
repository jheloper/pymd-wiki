from yaml import load
import src.const


class ConfigReader:

    def __init__(self):
        self.config = None

    def load_config(self, config_path=src.const.CONFIG_PATH):
        with open(config_path) as f:
            self.config = load(f)

    def get_config(self, config_key):
        return self.config.get(config_key)
