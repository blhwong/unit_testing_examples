from v1.s3 import upload
from v1.bert4rec import train
from v1.slack import post_message
from v1.db import complete_training, start_training


def generate_model_scores(model):
    log = start_training(model)
    output = train()
    upload(output)
    complete_training(log)
    post_message("#machine-learning", "Generate model scores complete")
