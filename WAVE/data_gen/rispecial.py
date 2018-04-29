import math
from random import shuffle, choice
import election
import csv


class Rispecial:
    num_approve = 0
    num_reject = 0
    total_ballots = 0
    filename = 'Election_Params.csv'

    def __init__(self):
        self._election = election.Election()

        self._gen_and_set_candidates()
        self.gen_ballots(self.filename)
        self._set_reported_results()

    def get_election(self): 
        return self._election
    
    def _gen_and_set_candidates(self):
        self._contestants = []

        self._contestants.append(election.Contestant(0, "Approve"))
        self._contestants.append(election.Contestant(1, "Reject"))

        self._election.set_contestants(self._contestants)

    def _set_reported_results(self):
        self._results = []

        self._results.append(election.Result(self._contestants[0], self.num_approve/self.total_ballots))
        self._results.append(election.Result(self._contestants[1], self.num_reject/self.total_ballots))

        self._election.set_reported_results(self._results)

    def get_reported_results(self):
        return self._results

    def gen_ballots(self, filename):
        ballots = []

        with open(filename, 'r') as csvfile:
            csvfile.readline()  # Skip first line
            readCSV = csv.reader(csvfile, delimiter=',')
            for cvr, precinct, ballot_style, vote in readCSV:
                ballot = election.Ballot()
                ballot.set_physical_ballot_num(int(cvr))

                ballots.append(ballot)
                self.total_ballots = self.total_ballots + 1
                if vote == 'Reject':
                    ballot.set_reported_value(self._contestants[1])
                    ballot.set_actual_value(self._contestants[1])
                    self.num_reject = self.num_reject + 1
                else:
                    ballot.set_reported_value(self._contestants[0])
                    ballot.set_actual_value(self._contestants[0])
                    self.num_approve = self.num_approve + 1


        for i, ballot in enumerate(ballots):
            ballot.set_audit_seq_num(ballot.get_physical_ballot_num())

        self._ballots = ballots
        self._election.set_ballots(ballots)
        print('BALLOTS LENGTH: ' + str(len(ballots)))
