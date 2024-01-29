from abc import ABC, abstractmethod


class AbstractStorage(ABC):
    @abstractmethod
    def upload(self, output):
        pass
