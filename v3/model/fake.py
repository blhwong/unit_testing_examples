from v3.model.abstract import AbstractModel


class FakeModel(AbstractModel):
    train_called = False
    def train(self):
        self.train_called = True
