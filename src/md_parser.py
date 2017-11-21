import markdown
from pathlib import Path

class MarkdownParser():

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