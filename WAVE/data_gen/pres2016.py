import math
import election


class Pres2016:
    def __init__(self):
        self._election = election.Election()

        self._gen_and_set_candidates()

    def get_election(self):
        return self._election()

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
        self._results = []

        self._results.append(election.Result(self._contestants[0], .544))
        self._results.append(election.Result(self._contestants[1], 0.389))
        self._results.append(election.Result(self._contestants[2], 0.032))
        self._results.append(election.Result(self._contestants[3], 0.02))
        self._results.append(election.Result(self._contestants[4], 0.013))
        self._results.append(election.Result(self._contestants[5], 0.001))
        
        self._election.set_reported_results(self._results)

    def _gen_ballots(self, count, error):
        sorted_results = sorted(self._results, 
                                key=lambda r: r.get_percentage,
                                reversed=True)

        ballot_count = []

        for i, result in enumerate(sorted_results):
            if i == 0:
                ballot_count.append(result.get_contestant(),
                                    math.floor((result.get_percentage() + error)
                                                * count))
            
            elif i == 1:
                ballot_count.append(result.get_contestant(),
                                    math.floor((result.get_percentage() - error)
                                                * count))

            else:
                ballot_count.append(result.get_contestant(),
                                    math.floor(result.get_percentage() * count))

        true_count = 0

        ballots = []

        for batch in ballot_count:
            for i in range(batch[1]):
                
