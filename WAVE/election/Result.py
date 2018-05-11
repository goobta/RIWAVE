class Result:
    def __init__(self, contestant, percentage, votes=0):
        self._contestant = contestant
        self._percentage = percentage
        self._votes = votes

    def get_contestant(self):
        return self._contestant

    def set_contestant(self, contestant):
        self._contestant = contestant

    def get_percentage(self):
        return self._percentage

    def set_percentage(self, percentage):
        self._percentage = percentage

    def set_votes(self, votes):
        self._votes = votes

    def get_votes(self):
        return self._votes
