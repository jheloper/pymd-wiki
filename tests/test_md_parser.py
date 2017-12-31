import unittest
import src.const as const
from src.md_parser import MarkdownParser


class TestMarkdownParser(unittest.TestCase):

    def test_set_get_source_path(self):
        md_parser = MarkdownParser()
        md_parser.set_source_path(const.PROJECT_TESTS_PATH + '/md_source')
        self.assertEqual(const.PROJECT_TESTS_PATH + '/md_source', md_parser.get_source_path())

    def test_set_get_target_path(self):
        md_parser = MarkdownParser()
        md_parser.set_target_path(const.PROJECT_TESTS_PATH + '/parsed_target')
        self.assertEqual(const.PROJECT_TESTS_PATH + '/parsed_target', md_parser.get_target_path())

    def test_parse_source_files_to_target_files(self):
        md_parser = MarkdownParser()
        md_parser.set_source_path(const.PROJECT_TESTS_PATH + '/md_source')
        md_parser.set_target_path(const.PROJECT_TESTS_PATH + '/parsed_target')
        md_parser.parse_source_files_to_target_files()
        self.assertEqual(len(list(md_parser.get_source_files_iterator())), len(list(md_parser.get_target_files_iterator())))


if __name__ == '__main__':
    unittest.main()
