class Result:
    def __init__(self, contestant, percentage):
        self._contestant = contestant
        self._percentage = percentage

    def get_contestant(self):
        return self._contestant

    def set_contestant(self, contestant):
        self._contestant = contestant

    def get_percentage(self):
        return self._percentage

    def set_percentage(self, percentage):
        self._percentage = percentage
