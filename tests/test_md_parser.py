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

    def test_read_files_in_source_path(self):
        md_parser = MarkdownParser()
        md_parser.set_source_path(const.PROJECT_TESTS_PATH + '/md_source')
        self.assertEqual(1, len(list(md_parser.get_source_files_iterator())))


if __name__ == '__main__':
    unittest.main()
