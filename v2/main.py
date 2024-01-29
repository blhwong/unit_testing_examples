from v2.db import DB
from v2.bert4rec import Bert4Rec
from v2.service import Service
from v2.s3 import S3
from v2.slack import Slack

if __name__ == '__main__':
    service = Service(DB(), Bert4Rec(), S3(), Slack())
    service.generate_model_scores("bert4rec")
