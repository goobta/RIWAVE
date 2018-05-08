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
        # Arbritary Starting Numbers - taken from Stark's paper
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
        # No discrepency in the ballot
        if ballot.get_actual_value() == ballot.get_reported_value():
            self._stopping_count -= 1
            return

        # If the ballot is an undervote
        if ballot.get_reported_value().get_id() == Undervote.CID:
            if ballot.get_actual_value().equals(self._winner):
                self._u1 += 1
            else:
                self._o1 += 1

        # If the ballot is an overvote
        elif ballot.get_reported_value().get_id() == Overvote.CID:
            if ballot.get_actual_value().equals(self._winner):
                self._u1 += 1
            else:
                self._ol += 1

        # If the ballot is a reported vote for the winner, but is really a vote for the
        # loser
        elif ballot.get_reported_value().equals(self_.winner) and \
                not ballot.get_actual_value(self._winner):
            self._o2 += 1

        # If the ballot is a reported vote for a loser, but is really a vote for the 
        # winner
        elif not ballot.get_reported_value().equals(self._winner) and \
                ballot.get_actual_value().equals(self._winner):
            self._u2 += 1

        # Error handling
        else:
            print("Error processing ballot {}".format(ballot.get_physical_ballot_num()))
            print("Actual: {}".format(ballot.get_actual_value().get_name()))
            print("Reported: {}".format(ballot.get_reported_value().get_name()))

        # Recacluate count using Stark's formula
        self._stopping_count = -2 * self._inflator * ( \
                log(self._risk_limit) + \
                self._o1 * log(1 - 1 / (2 * self._inflator)) + \
                self._o2 * log(1 - 1 / self._inflator) + \
                self._u1 * log(1 + 1 / (2 * self._inflator)) + \
                self._u2 * log(1 + 1 / self._inflator)) \
                / self._diluted_margin

        # Update status
        self._refresh_status()

    def _refresh_status(self):
        if self._stopping_count == 0:
            self._status = 1
        else:
            self._status = 0

    def recompute(self, ballots, results):
       pass

    def get_current_result(self):
       pass

