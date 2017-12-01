from numpy import inf
from flatparser import Parser
import sys
from util import Stack
import numpy as np
import time

uptime = {}

start_time = time.time()

problem = Parser(sys.argv[1])

end_time = time.time()
uptime['parsing'] = end_time - start_time

states = problem.states
actions = problem.action

values = dict()
policy = dict()

solvState = {state: False for state in states} # creates dict that relates a state to a solved status, beginning with all False

for stat in states:
    values[stat] = 0

for goal in problem.goalState:
    solvState[goal] = True

def greedyAction(s): # s - State
    qvalue = inf
    action = None
    for a in actions:
        newq = qValue(s,a)
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

    if s in problem.goalState:
        return 0 + problem.discount_factor * somatoria
    else:
        return 1 + problem.discount_factor * somatoria

def update(s): # s - state
    a = greedyAction(s)
    values[s] = qValue(s, a)
    policy[s] = a

def pickNextState(a, s): # stochastically selects next state given an action 'a' e current state 's'
    des = []
    pro = []
    for nxt in actions[a]:
        orig, dest, prob = nxt.getDatas()
        if (orig == s):
            des.append(dest)
            pro.append(prob)
    valDest = []
    proDest = []
    for i in range(len(des)):
        if solvState[des[i]]:
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
    #return dest

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
        #print(s, len(openList))
        closedList.push(s)
        if residual(s) > resid:
            rv = False
            continue
        a = greedyAction(s)
        for nxt in actions[a]:
            orig, dest, prob = nxt.getDatas()
            if ((orig == s) and (prob > 0)):
                if not solvState[dest] and not openList.hasItem(dest) and not closedList.hasItem(dest):
                    openList.push(dest)
    
    if rv:
        for i in range(len(closedList)):
            pastState = closedList.pop()
            solvState[pastState] = True
    else:
        while not closedList.isEmpty():
            sNxt = closedList.pop()
            update(sNxt)
    return rv


def lrtdpTrial(s, resid):
    visited = Stack()
    while not solvState[s]:
        visited.push(s)
        if s in problem.goalState:
            break
        a = greedyAction(s)
        update(s)
        lastState = s
        s = pickNextState(a, s)
        #print("oi")
        if (lastState == s):
            break
    while not visited.isEmpty():
        #print("tchau")
        s = visited.pop()
        if not checkSolved(s, resid):
            #print("sai do checkSolved")
            break
    #print(solvState)

init = problem.initState
err = 0

start_time = time.time()

while not solvState[init]:
    lrtdpTrial(init, err)

end_time = time.time()
end_time = time.time()
uptime['valueIteration'] = end_time - start_time

print('>> Policy')
for p in policy:
    print(p, '->', policy[p])

print('\n>> Time: parsing = {0:.4f}, solving = {1:.4f}'.format(
        uptime['parsing'], uptime['valueIteration']))