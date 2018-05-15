import audit
import election


class Bayesian(audit.Audit):
    name = "Bayesian Audit"
    status_codes = ["In Progress", 
                    "Election Results Verified",
                    "Full Hand Count Required"]

    def __init__(self):
        self.risk_limit_m = -1
        self.risk_upset_m = -1
        self.pseudocount_base = 0.5
        self.pseudocount_match = 50.0
        self.n_trials = 100000

        self.status = 0

    def init(self, results):
        pass

    def get_progress(self):
        pass 

    def get_status(self):
        return Bayesian.status_codes[self.status]

    @staticmethod
    def get_name():
        return Bayesian.name

    def get_parameters(self):
        param = [["Risk Limit", str(self.risk_limit_m)],
                 ["Risk Upset", str(self.risk_upset_m)]]
                
        return param

    def set_parameters(self, param):
        pass

    def recompute(self, ballots, results):
        pass

    def compute(self, ballot):
        pass

    def get_current_result(self):
        pass
