import math
import audit
import election

"""
Based off of Dr. Stark's "Super-Simple Simultaneous Single-ballot Risk Limiting Audits"
"""

class Comparision(audit.Audit):
    name = "Comparision RLA"
    status_codes = ["In Progress",
                    "Election Results Verified"]

    def __init__(self):
        # Arbritary Numbers - Numbers taken from Stark's paper
        self._risk_limit = 5
        self._inflator = 1.03905
        self._o1_expected = 0.001
        self._o2_expected = 0.0001
        self._u1_expected = 0.001
        self._u2_expected = 0.0001

        self._o1 = 0
        self._o2 = 0
        self._u1 = 0
        self._u2 = 0
        self._stopping_count = 0
        self._diluted_margin = 0
        self._status = 0

    def init(self, results, ballot_count):
        results_sorted = sorted(results,
                                key=lambda r: r.get_percentage(),
                                reverse=True)

        margin = results_sorted[0].get_votes() - results_sorted[1].get_votes()
        self._diluted_margin = margin / self._risk_limit

    def get_progress(self):
        pass

    def get_status(self):
        return Comparision.status_codes[self._status]

    @staticmethod
    def get_name():
        return Comparision.name

    def get_parameters(self):
        param = [["Risk Limit", self._alpha],
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

