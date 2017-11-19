class Problem():
    initState = ""
    goalState = ""
    discount_factor = 0
    action = {}
    states = {}

    def __init__(self,initState,goalState,discont_fator,action,states):
        self.initState = initState
        self.goalState = goalState
        self.discount_factor = discont_fator
        self.action = action
        self.states = states

    def __str__(self):
        string = "Estado inicial:" + self.initState + "\n" \
                +"Estado final:" + self.goalState + "\n" \
                +"Fator de disconto:" + str(self.discount_factor) + "\n" \
                +"Acoes:" + str(self.action) + "\n" \
                +"Estados:" + str(self.states)
        return string