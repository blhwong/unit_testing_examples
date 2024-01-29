from v3.notification.abstract import AbstractNotification


class Sendgrid(AbstractNotification):
    def post_message(self, channel, message):
        print(f"Start post_message. channel={channel} message={message}")


