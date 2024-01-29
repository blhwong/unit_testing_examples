from datetime import datetime

from v3.db.abstract import AbstractDB


class PostgresDB(AbstractDB):
    def start_training(self, model):
        print(f"Log training start. model={model}")
        return {"model": model, "started_at": datetime.now()}

    def complete_training(self, log):
        log.update({"completed_at": datetime.now()})
        print(f"Log training complete. log={log}")
        return log

