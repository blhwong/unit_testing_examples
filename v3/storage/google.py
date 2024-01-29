from v3.storage.abstract import AbstractStorage


class Spreadsheet(AbstractStorage):
    def upload(self, output):
        print(f"Start upload. output={output}")

