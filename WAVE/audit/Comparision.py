from math import log
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

        self._winner = None

    def init(self, results, ballot_count):
        self._o1 = 0
        self._o2 = 0
        self._u1 = 0
        self._u2 = 0

        results_sorted = sorted(results,
                                key=lambda r: r.get_percentage(),
                                reverse=True)

        self._winner = results_sorted[0].get_contestant()

        margin = results_sorted[0].get_votes() - results_sorted[1].get_votes()
        self._diluted_margin = margin / self._risk_limit
        self._stopping_count = -2 * self._inflator * log(self._risk_limit) / ( \
                self._diluted_margin + 2 * self._inflator * ( \
                    self._o1_expected * log(1 - (1 / (2 * self._inflator))) + \
                    self._o2_expected * log(1 - (1 / self._inflator)) + \
                    self._u1_expected * log(1 + (1 / (2 * self._inflator))) + \
                    self._u2_expected * log(1 + (1 / self._inflator))
                    )
                )

    def get_progress(self):
        return "{} correct ballots left".format(self._stopping_count)

    def get_status(self):
        return Comparision.status_codes[self._status]

    @staticmethod
    def get_name():
        return Comparision.name

    def get_parameters(self):
        param = [["Risk Limit", str(self._alpha)],
                 ["Error Inflation Factor", str(self._inflator)],
                 ["Expected 1-vote Overstatement Rate", str(self._o1_expected)],
                 ["Expected 2-vote Overstatement Rate", str(self._o2_expected)],
                 ["Expected 1-vote Understatement Rate", str(self._u1_expected)],
                 ["Expected 2-vote Understatement Rate", str(self._u2_expected)]]

        return param

    def set_parameters(self, param):
        self._risk_limit = int(param[0])
        self._inflator = float(param[1])
        self._o1_expected = float(param[2])
        self._o2_expected = float(param[3])
        self._u1_expected = float(param[4])
        self._u2_expected = float(param[5])

        self.recompute()

    def compute(self, ballot):
       pass

    def recompute(self, ballots, results):
       pass

    def get_current_result(self):
       pass

