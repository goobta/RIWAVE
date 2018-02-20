import election
import audit
import data_gen
import sys


if __name__ != "__main__":
    sys.exit(1)

pres = data_gen.Pres2016()
pres.gen_ballots(1000, .00)

e = pres.get_election()

for i, ballot in enumerate(e.get_ballots()):
    print("Ballot " + str(ballot.get_audit_seq_num()) + " Reported Value " + str(ballot.get_reported_value().get_name()) + " Actual value " + str(ballot.get_actual_value().get_name()))

rla = audit.RLA()
rla.init(pres.get_reported_results())

rla.set_parameters([0.01])
rla.recompute(e.get_ballots(), pres.get_reported_results())

print(rla.get_progress())
