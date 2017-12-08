from numpy import inf
from ppddlparser import Parser
import sys
import time

class ValueIteration():
    def __init__(self,problem):
        self.uptime = {}

        self.problem = problem

        self.states = self.problem.states
        self.actions = self.problem.action

        self.values = dict()
        self.policy = dict()


    # def __init__(self,arquivo):
    #     self.uptime = {}
    #
    #     start_time = time.time()
    #
    #     self.problem = Parser(arquivo)
    #
    #     end_time = time.time()
    #     self.uptime['parsing'] = end_time - start_time
    #
    #     self.states = self.problem.states
    #     self.actions = self.problem.action
    #
    #     self.values = dict()
    #     self.policy = dict()


    def planejar(self):

        # start_time = time.time()

        for s in self.states:
            self.values[s] = self.states[s] # get state reward from 'states' dictionary

        n = 0
        converge =  False
        threshold = 0.0
        while not converge:
            n += 1
            val = dict()
            for s in self.states:
                qvalue = -inf
                for a in self.actions:
                    somatoria = 0
                    for nxt in self.actions[a]:
                        orig, dest, prob = nxt.getDatas()
                        if (orig == s):
                            somatoria += prob * self.values[dest]
                    newq = self.states[s] + self.problem.discount_factor * somatoria
                    if newq > qvalue:
                        val[s] = newq
                        self.policy[s] = a
                        qvalue = newq
            for v in val:
                if abs(val[v] - self.values[v]) > threshold:
                    converge = False
                else:
                    converge = True
            self.values = val.copy()

        # end_time = time.time()
        # self.uptime['valueIteration'] = end_time - start_time
        #
        # print('>> Policy')
        # for p in self.policy:
        #     print(p, '->', self.policy[p])
        #
        # print('\n>> Time: parsing = {0:.4f}, solving = {1:.4f}'.format(
        #     self.uptime['parsing'], self.uptime['valueIteration']))