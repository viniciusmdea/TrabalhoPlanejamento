class Action():
    def __init__(self,fromState,toState,probability=0.0,cost=0):
        self._fromState = fromState
        self._toState = toState
        self._probability = probability
        self._cost = cost

    @property
    def fromState(self):
        return self._fromState

    @property
    def toState(self):
        return self._toState

    @property
    def prob(self):
        return self._prob
    
    @property
    def cost(self):
        return self._cost

    def __str__(self):
        string = "Inicial:" + str(self._fromState) + "\n" \
                +"Final:" + str(self._toState) + "\n"
        return string

    def getDatas(self):
        return self._fromState, self._toState,self._probability