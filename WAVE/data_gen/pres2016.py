import election


class Pres2016:
    def __init__(self):
        self._election = election.Election()

        self._gen_and_set_candidates()

    def _gen_and_set_candidates(self):
        self._contestants = []

        self._contestants.append(election.Contestant(0, "Hillary Clinton"))
        self._contestants.append(election.Contestant(1, "Donald J. Trump"))
        self._contestants.append(election.Contestant(2, "Gary Johnson"))
        self._contestants.append(election.Contestant(3, "Write In"))
        self._contestants.append(election.Contestant(4, "Jill Stein"))
        self._contestants.append(election.Contestant(5, "Roque De La Fuente"))

        self._election.set_contestants(self._contestants)

    def _set_reported_results(self):
       results = []

       results.append(election.Result(self._contestants[0], .544))
       results.append(election.Result(self._contestants[1], 0.389))
       results.append(election.Result(self._contestants[2], 0.032))
       results.append(election.Result(self._contestants[3], 0.02))
       results.append(election.Result(self._contestants[4], 0.013))
       results.append(election.Result(self._contestants[5], 0.001))

       self._election.set_reported_results(results)

