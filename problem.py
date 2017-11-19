class Problem():
    def __init__(self, initState, goalState, discount_factor, action, states):
        self._initState = initState
        self._goalState = goalState
        self._discount_factor = discount_factor
        self._action = action
        self._states = states

    @property
    def initState(self):
        return self._initState

    @property
    def goalState(self):
        return self._goalState

    @property
    def discount_factor(self):
        return self._discount_factor
    @property
    def action(self):
        return self._action
    
    @property
    def states(self):
        return self._states

    def __str__(self):
        string = "Estado inicial:" + self.initState + "\n" \
                +"Estado final:" + self.goalState + "\n" \
                +"Fator de disconto:" + str(self.discount_factor) + "\n" \
                +"Acoes:" + str(self.action) + "\n" \
                +"Estados:" + str(self.states)
        return string