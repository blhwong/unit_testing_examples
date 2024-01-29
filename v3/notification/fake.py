from v3.notification.abstract import AbstractNotification


class FakeNotification(AbstractNotification):
    post_message_called = False
    def post_message(self, channel, message):
        self.post_message_called = True
