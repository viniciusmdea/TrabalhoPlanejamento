from numpy import inf
import Parser

problem = Parser.Parser("navigation01.net")
#print (problem)

#negative infinite -inf
states = problem.states
actions = problem.action

values = dict()
policy = dict()
for s in states:
    values[s] = states[s] # get state reward from 'states' dictionary

n = 0 # desne
converge =  False
while not converge:
    n += 1
    val = dict() # dict()
    for s in states:
        qvalue = -inf
        for a in actions:
            somatoria = 0
            for nxt in actions[a]:
                orig, dest, prob = nxt.getDatas()
                if (orig == s):
                    somatoria += prob * values[dest]
            newq = states[s] + problem.discount_factor* somatoria
            if newq > qvalue:
                val[s] = newq
                policy[s] = a
    for v in val: # get key in val
        if abs(val[v] - values[v]) > 0.1:
            converge = False
        else:
            converge = True
    values = val.copy()

print("Policy",policy)

# implement loop to extract policy
# policy is automatically being updated