from abc import ABC, abstractmethod


class AbstractNotification(ABC):
    @abstractmethod
    def post_message(self, channel, message):
        pass
