from v3.storage.abstract import AbstractStorage


class FakeStorage(AbstractStorage):
    upload_called = False
    def upload(self, output):
        self.upload_called = True
