import unittest
from src.config_reader import ConfigReader


class ConfigReaderTest(unittest.TestCase):

    def test_load_config(self):
        cr = ConfigReader()
        cr.load_config()
        self.assertIsNotNone(cr.config)

    def test_get_config(self):
        cr = ConfigReader()
        cr.load_config()
        print(cr.get_config('site-title'))
        self.assertIsNotNone(cr.get_config('site-title'))


if __name__ == '__main__':
    unittest.main()
