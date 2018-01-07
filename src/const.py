from os.path import abspath, dirname

PROJECT_ROOT_PATH = dirname(dirname(abspath(__file__)))
PROJECT_SOURCE_PATH = PROJECT_ROOT_PATH + '/src'
PROJECT_TESTS_PATH = PROJECT_ROOT_PATH + '/tests'

CONFIG_PATH = PROJECT_ROOT_PATH + '/config.yml'
