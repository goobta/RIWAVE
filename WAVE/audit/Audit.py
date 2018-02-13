from abc import ABC

class Audit(ABC):
    @abstractmethod
    def get_progress(self):
