from numpy import inf
from flatparser import Parser
import sys
from util import Stack
import numpy as np
import time

class Lrtdp:

    def __init__(self,problem):
        self.problem = problem
        self.states = problem.states
        self.actions = problem.action

        self.values = dict()
        self.policy = dict()

        self.solvState = {state: False for state in self.states}  # creates dict that relates a state to a solved status, beginning with all False

        for stat in self.states:
            self.values[stat] = 0

        for goal in problem.goalState:
            self.solvState[goal] = True

    def greedyAction(self,s):  # s - State
        qvalue = inf
        action = None
        for a in self.actions:
            newq = self.qValue(s, a)
            if newq < qvalue:
                qvalue = newq
                action = a
        return action

    def qValue(self,s, a):  # a - Action, s - State
        somatoria = 0
        for nxt in self.actions[a]:
            orig, dest, prob = nxt.getDatas()
            if (orig == s):
                somatoria += prob * self.values[dest]

        if s in self.problem.goalState:
            return 0 + self.problem.discount_factor * somatoria
        else:
            return 1 + self.problem.discount_factor * somatoria

    def update(self,s):  # s - state
        a = self.greedyAction(s)
        self.values[s] = self.qValue(s, a)
        self.policy[s] = a

    def pickNextState(self,a, s):  # stochastically selects next state given an action 'a' e current state 's'
        des = []
        pro = []
        for nxt in self.actions[a]:
            orig, dest, prob = nxt.getDatas()
            if (orig == s):
                des.append(dest)
                pro.append(prob)
        valDest = []
        proDest = []
        for i in range(len(des)):
            if self.solvState[des[i]]:
                continue
            valDest.append(des[i])
            proDest.append(pro[i])
        for j in range(len(proDest)):
            proDest[j] = proDest[j] / sum(proDest)
        if len(valDest) > 0:
            return np.random.choice(valDest, p=proDest)
        else:
            return s
            # for nxt in actions[a]:
            #     orig, dest, prob = nxt.getDatas()
            #     if (orig == s):
            #         k += prob
            #         if (rand < k):
            #             break
            # return dest

    def residual(self,s):  # s - state
        a = self.greedyAction(s)
        return abs(self.values[s] - self.qValue(s, a))

    def checkSolved(self,s, resid):  # state (String) s and Residual float value resid
        rv = True
        openList = Stack()
        closedList = Stack()
        if (self.solvState[s] == False):
            openList.push(s)
        while not openList.isEmpty():
            s = openList.pop()
            # print(s, len(openList))
            closedList.push(s)
            if self.residual(s) > resid:
                rv = False
                continue
            a = self.greedyAction(s)
            for nxt in self.actions[a]:
                orig, dest, prob = nxt.getDatas()
                if ((orig == s) and (prob > 0)):
                    if not self.solvState[dest] and not openList.hasItem(dest) and not closedList.hasItem(dest):
                        openList.push(dest)

        if rv:
            for i in range(len(closedList)):
                pastState = closedList.pop()
                self.solvState[pastState] = True
        else:
            while not closedList.isEmpty():
                sNxt = closedList.pop()
                self.update(sNxt)
        return rv

    def lrtdpTrial(self,s, resid):
        visited = Stack()
        while not self.solvState[s]:
            visited.push(s)
            if s in self.problem.goalState:
                break
            a = self.greedyAction(s)
            self.update(s)
            lastState = s
            s = self.pickNextState(a, s)
            # print("oi")
            if (lastState == s):
                break
        while not visited.isEmpty():
            # print("tchau")
            s = visited.pop()
            if not self.checkSolved(s, resid):
                # print("sai do checkSolved")
                break
                # print(solvState)


    def iniciar(self):
        init = self.problem.initState
        err = 0

        while not self.solvState[init]:
            self.lrtdpTrial(init, err)

        # print('>> Policy')
        # for p in self.policy:
        #     print(p, '->', self.policy[p])

