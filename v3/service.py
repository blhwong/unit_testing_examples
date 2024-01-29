from v3.storage.abstract import AbstractStorage
from v3.db.abstract import AbstractDB
from v3.model.abstract import AbstractModel
from v3.notification.abstract import AbstractNotification


class Service:

    def __init__(self, db: AbstractDB, model: AbstractModel, storage: AbstractStorage, notification: AbstractNotification):
        self.db = db
        self.model = model
        self.storage = storage
        self.notification = notification

    def generate_model_scores(self, model):
        log = self.db.start_training(model)
        output = self.model.train()
        self.storage.upload(output)
        self.db.complete_training(log)
        self.notification.post_message("#machine-learning", "Generate model scores complete")
