import markdown
from pathlib import Path


class MarkdownParser:

    def __init__(self):
        self.source_path = None
        self.target_path = None

    def set_source_path(self, source_path):
        self.source_path = source_path

    def get_source_path(self):
        return self.source_path

    def set_target_path(self, target_path):
        self.target_path = target_path

    def get_target_path(self):
        return self.target_path

    def get_source_files_iterator(self):
        return Path(self.get_source_path()).iterdir()

    def get_target_files_iterator(self):
        return Path(self.get_target_path()).iterdir()

    def parse_source_files_to_target_files(self):
        source_file_iterator = self.get_source_files_iterator()
        for source_file in source_file_iterator:
            Path(self.get_target_path()).mkdir(exist_ok=True)
            target_file = self.get_target_path() + '/' + source_file.with_suffix('.html').name
            with open(source_file) as f:
                markdown_content = markdown.markdown(f.read())
                Path(target_file).open('w').write(markdown_content)
