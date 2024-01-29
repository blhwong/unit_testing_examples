from v2.s3 import S3
from v2.db import DB
from v2.bert4rec import Bert4Rec
from v2.slack import Slack


class Service:

    def __init__(self, db: DB, model: Bert4Rec, s3: S3, slack: Slack):
        self.db = db
        self.model = model
        self.s3 = s3
        self.slack = slack

    def generate_model_scores(self, model):
        log = self.db.start_training(model)
        output = self.model.train()
        self.s3.upload(output)
        self.db.complete_training(log)
        self.slack.post_message("#machine-learning", "Generate model scores complete")
