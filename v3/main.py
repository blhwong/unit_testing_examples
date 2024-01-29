from v3 import settings
from v3.db.postgres import PostgresDB
from v3.db.snowflake import SnowflakeDB
from v3.model.bert4rec import Bert4Rec
from v3.model.lightfm import LightFM
from v3.notification.sendgrid import Sendgrid
from v3.service import Service
from v3.storage.s3 import S3
from v3.notification.slack import Slack
from v3.storage.google import Spreadsheet


if __name__ == '__main__':
    if settings.implementation_version == "use_case1":
        service = Service(SnowflakeDB(), Bert4Rec(), S3(), Slack())
        service.generate_model_scores("bert4rec")
    elif settings.implementation_version == "use_case2":
        service = Service(PostgresDB(), LightFM(), Spreadsheet(), Sendgrid())
