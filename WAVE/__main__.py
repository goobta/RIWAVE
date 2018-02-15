import WAVE.election
import WAVE.audit
import WAVE.data_gen
import sys


if __name__ != "__main__":
    sys.exit(1)

pres = WAVE.data_gen.Pres2016()
pres.gen_ballots(1000, .03)

e = pres.get_election()

for i, ballot in enumerate(e.get_ballots()):
    print("Ballot")
    print(ballot.get_audit_seq_num())
    print("Reported Value")
    print(ballot.get_reported_value().get_name())
    print("Actual value")
    print(ballot.get_actual_value().get_name())
    print("\n")

rla = WAVE.audit.RLA()
rla.init(pres.get_reported_results())

rla.set_parameters([0.01])
rla.recompute(e.get_ballots(), pres.get_reported_results())

print(rla.get_progress())
