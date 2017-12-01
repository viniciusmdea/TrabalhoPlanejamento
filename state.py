class State():
    def __init__(self, solved=False): # self, name, solved=False
        # self._name = name
        self._solved = solved

    # @property
    # def name(self):
    #     return self._name

    @property
    def solved(self):
        return self._solved
