from v3.db.abstract import AbstractDB


class FakeDB(AbstractDB):
    start_training_called = False
    complete_training_called = False

    def start_training(self, model):
        self.start_training_called = True

    def complete_training(self, log):
        self.complete_training_called = True
