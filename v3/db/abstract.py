from abc import ABC, abstractmethod


class AbstractDB(ABC):
    @abstractmethod
    def start_training(self, model):
        pass

    @abstractmethod
    def complete_training(self, log):
        pass
