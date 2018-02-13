from abc import ABC

class Audit(ABC):
    @abstractmethod
    def get_progress(self):
        pass

    @abstractmethod
    def get_status(self):
        pass

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_parameters(self):
        pass

    @abstractmethod
    def set_parameters(self, param):
        pass

    @abstractmethod
    def recompute(self, ballot):
        pass

    @abstractmethod
    def get_current_result(self):
        pass
