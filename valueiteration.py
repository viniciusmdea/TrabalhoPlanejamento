from numpy import inf
from ppddlparser import Parser
import sys
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

start_time = time.time()

for s in states:
    values[s] = states[s] # get state reward from 'states' dictionary

n = 0
converge =  False
threshold = 0.0
while not converge:
    n += 1
    val = dict()
    for s in states:
        qvalue = -inf
        for a in actions:
            somatoria = 0
            for nxt in actions[a]:
                orig, dest, prob = nxt.getDatas()
                if (orig == s):
                    somatoria += prob * values[dest]
            newq = states[s] + problem.discount_factor * somatoria
            if newq > qvalue:
                val[s] = newq
                policy[s] = a
                qvalue = newq
    for v in val:
        if abs(val[v] - values[v]) > threshold:
            converge = False
        else:
            converge = True
    values = val.copy()
end_time = time.time()
uptime['valueIteration'] = end_time - start_time

print('>> Policy')
for p in policy:
    print(p, '->', policy[p])

print('\n>> Time: parsing = {0:.4f}, solving = {1:.4f}'.format(
        uptime['parsing'], uptime['valueIteration']))