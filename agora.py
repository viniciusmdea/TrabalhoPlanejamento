from numpy import inf
from ppddlparser import Parser
import sys
from util import Stack
import random

problem = Parser(sys.argv[1])
states = problem.states
actions = problem.action

values = dict()
policy = dict()

solvState = {state: False for state in states} # creates dict that relates a state to a solved status, beginning with all False

for stat in states:
    values[stat] = 0

solvState[problem.goalState] = True

def greedyAction(s): # s - State
    qvalue = inf
    action = None
    #print(s)
    #options = set()
    for a in actions:
        newq = abs(qValue(s,a)) 
        #print(a,newq)
        #print(newq, s, a)
        if newq < qvalue:
            qvalue = newq
            action = a
    return action


def qValue(s, a): # a - Action, s - State
    somatoria = 0
    for nxt in actions[a]:
        orig, dest, prob = nxt.getDatas()
        if (orig == s):
            somatoria += prob * values[dest]
    return states[s] + somatoria
    # return a.cost + somatoria

def update(s): # s - state
    a = greedyAction(s)
    values[s] = qValue(s, a)
    #policy[s] = a

def pickNextState(a, s): # stochastically selects next state given an action 'a' e current state 's'
    rand = random.uniform(0,1)
    k = 0
    for nxt in actions[a]:
        orig, dest, prob = nxt.getDatas()
        if (orig == s):
            k += prob
            if (rand < k):
                break
    return dest

def residual(s): # s - state
    a = greedyAction(s)
    return abs(values[s] - qValue(s,a))

def checkSolved(s, resid): # state (String) s and Residual float value resid
    rv = True
    openList = Stack()
    closedList = Stack()
    if (solvState[s] == False):
        openList.push(s)
    while not openList.isEmpty():
        s = openList.pop()
        closedList.push(s)
        if residual(s) > resid:
            rv = False
            continue

        a = greedyAction(s)
        for nxt in actions[a]:
            orig, dest, prob = nxt.getDatas()
            if ((orig == s) and (prob > 0)):
                if not solvState[dest] and not openList.hasItem(dest):
                    openList.push(dest)
    if rv:
        for i in range(len(closedList)):
            s = closedList.pop()
            solvState[s] = True
    else:
        while not closedList.isEmpty():
            sNxt = closedList.pop()
            update(sNxt)
    return rv


def lrtdpTrial(s, resid):
    visited = Stack()
    lastState = None
    while not solvState[s] and len(visited) < 30:
        visited.push(s)
        if problem.goalState == s:
            break
        a = greedyAction(s)
        update(s)
        s = pickNextState(a, s)
    while not visited.isEmpty():
        s = visited.pop()
        if not checkSolved(s, resid):
            break

init = problem.initState
err = 1.0
while not solvState[init]:
    #import pdb; pdb.set_trace()
    lrtdpTrial(init, err)
    #s = problem.initState


print('>> Values')
for p in values:
    print(p, '->', values[p])