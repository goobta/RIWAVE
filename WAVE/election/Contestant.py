class Contestant:
    def __init__(self, ID, name):
        self._id = ID
        self._name = name

    def get_id(self):
        return self._id

    def set_id(self, ID):
        self._id = ID

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def equals(self, contestant):
        if isinstance(contestant, Contestant):
            if contestant.get_name() == self.get_name():
                return True

        return False

class Undervote(Contestant):
    CID = -2

    def __init__(self):
        super().__init__(Undervote.CID, "undervote")

class Overvote(Contestant):
    CID = -3 

    def __init__(self):
        super().__init__(Overvote.CID, "overvote")
