from v3.storage.abstract import AbstractStorage


class S3(AbstractStorage):
    def upload(self, output):
        print(f"Start upload. output={output}")

