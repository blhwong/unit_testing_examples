from v3.model.abstract import AbstractModel


class Bert4Rec(AbstractModel):
    def train(self):
        print("Start training.")
        return { "a@a.com": [1, 2, 3], "b@b.com": [2, 3, 1], "c@c.com": [3, 2, 1]}

