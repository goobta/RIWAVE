import math
import audit
import election

"""
Based off of Dr. Stark's "Super-Simple Simultaneous Single-ballot Risk Limiting Audits"
"""

class Comparision(audit.Audit):
    name = "Comparision RLA"
    status_codes = ["In Progress",
                    "Election Results Verified",
                    "Full Hand Count Required"]

    def __init__(self):
        self._status = 0
        self._alpha = 0.0
        self._gamma = 0.0
        self._lambda = 0.0
        self._mu = -1
        self._rho = 0

    def init(self, results):
        self._rho = (-math.log10(self._alpha)) / 
                    ((1 / (2 * self._gamma)) + 
                        self._lambda * math.log10(1 - (1 / (2 * self._gamma))))
        self._mu = 

    def get_progress(self):
        pass

    def get_status(self):
        return Comparision.status_codes[self._status]

    @staticmethod
    def get_name():
        return Comparision.name

    def get_parameters(self):
        param = [
                ["Risk Limit", self._alpha],
                ["Error Inflation Factor", self._gamma],
                ["Tolerance", self._lambda]]

        return param

    def set_parameters(self, param):
        self._alpha = float(param[0])
        self._gamma = float(param[1])
        self._lambda = float(param[2])

    def compute(self, ballot):
       pass

    def recompute(self, ballots, results):
       pass

    def get_current_result(self):
       pass

    def _e(self, ballot):
       pass

