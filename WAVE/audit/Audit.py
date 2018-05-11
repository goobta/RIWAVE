from abc import ABC, abstractmethod


class Audit(ABC):
    @abstractmethod
    def init(self, results, ballot_count):
        pass

    @abstractmethod
    def get_progress(self):
        pass

    @abstractmethod
    def get_status(self):
        pass

    @staticmethod
    @abstractmethod
    def get_name():
        return "Select Audit"

    @abstractmethod
    def get_parameters(self):
        pass

    @abstractmethod
    def set_parameters(self, param):
        pass

    @abstractmethod
    def recompute(self, ballots, results):
        pass

    @abstractmethod
    def compute(self, ballot):
        pass

    @abstractmethod
    def get_current_result(self):
        pass
