class Action():
    fromState = ""
    toState = ""
    probability = 0
    cost = 0

    def __init__(self,fromState,toState,probability=0.0,cost=0):
        self.fromState = fromState
        self.toState = toState
        self.probability = probability
        self.cost = cost

    def __str__(self):
        string = "Inicial:" + str(self.fromState) + "\n" \
                +"Final:" + str(self.toState) + "\n"
        return string

    def getDatas(self):
        return self.fromState,self.toState,self.probability