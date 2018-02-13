class Ballot:
    def __init__(self):
        self._audit_seq_num = -1
        self._physical_ballot_num = -1
        self._reported_value = None
        self._actual_value = None

    def get_audit_seq_num(self):
        return self._audit_seq_num

    def set_audit_seq_num(self, audit_seq_num):
        self._audit_seq_num = audit_seq_num

    def get_physical_ballot_num(self):
        return self._physical_ballot_num

    def set_physical_ballot_num(self, physical_ballot_num):
        self._physical_ballot_num = physical_ballot_num

    def get_reported_value(self):
        return self._reported_value

    def set_reported_value(self, reported_value):
        self._reported_value = reported_value

    def get_actual_value(self):
        return self._actual_value

    def set_actual_value(self, actual_value):
        self._actual_value = actual_value

