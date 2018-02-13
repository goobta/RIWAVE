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
