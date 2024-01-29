def start_training(model):
    return {}

def train():
    return {}

def upload(output):
    pass

def complete_training(log):
    pass

def post_message(channel, message):
    pass

def generate_model_scores(model):
    log = start_training(model)
    output = train()
    upload(output)
    complete_training(log)
    post_message("#machine-learning", "Generate model scores complete")

if __name__ == '__main__':
    generate_model_scores("bert4rec")
