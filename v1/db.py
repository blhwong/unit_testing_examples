from datetime import datetime


def start_training(model):
    print(f"Log training start. model={model}")
    return { "model": model, "started_at": datetime.now()}

def complete_training(log):
    log.update({"completed_at": datetime.now()})
    print(f"Log training complete. log={log}")
    return log

