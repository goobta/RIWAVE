import audit
import election


class Bayesian(audit.Audit):
    def init(self, results):
        pass

    def get_progress(self):
        pass

    def get_status(self):
        pass

    @staticmethod
    def get_name():
        return "Bayesian"

    def get_parameters(self):
        pass

    def set_parameters(self, param):
        pass

    def recompute(self, ballots, results):
        pass

    def compute(self, ballot):
        pass

    def get_current_result(self):
        pass
