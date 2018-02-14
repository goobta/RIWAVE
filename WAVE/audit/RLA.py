import WAVE.audit as audits


class RLA(audits.Audit):
    name = "Risk Limiting Audit"
    status_codes = ["In Progress", 
                    "Election Results Verified",
                    "Full Hand Count Required"]

    def __init__(self):
        self._T = 1
        self._tolerance = -1
        self._s = -1
        self._margin = -1
        self._winner = -1

        self._status = 0
        self._cached_results = list()

    def init(self, results):
        self.__init__()

        results_sorted = sorted(results, 
                                key=lambda r: r.get_percentage(),
                                reverse=True)

        self._s = results_sorted[0].get_percentage()
        self._winner = results_sorted[0].get_contestant()
        self._margin = self._s - self._tolerance

        for result in results:
            self._cached_results.append([result.get_contestant(), 0])

    def get_progress(self):
        return "T = " + str(self._T)

    def get_status(self):
        return RLA.status_codes[self._status]

    def get_name(self):
        return RLA.name

    def get_parameters(self):
        param = ["Tolerance"]
        
        return param

    def set_parameters(self, param):
        self._tolerance = param[0]

    def compute(self, ballot):
        ballot_vote = ballot.get_actual_value()

        if ballot_vote.equals(self._winner):
            self._T *= self._margin / .50
        else:
            self._T += (1 - self._margin) / .50

        for i in range(len(self._cached_results)):
            if self._cached_results[i][0].equals(ballot_vote):
                self._cached_results[i][1] += 1
                break

        self._refresh_status()

    def _refresh_status(self):
        if self._T > 9.9:
            self._status = 1
        elif self._T < 0.011:
            self._status = 2
        else:
            self._status = 0

    def recompute(self, ballots, results):
        self.init(results)

        for ballot in ballots:
            self.compute(ballot)

    def get_current_result(self):
        count = 0

        for result in self._cached_results:
            count += result[1]

        audit_results = []

        for person in self._cached_results:
            result = Result(person[0], person[1] / count)
            audit_results.append(result)

        reutrn audit_results
