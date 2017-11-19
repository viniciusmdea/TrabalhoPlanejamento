## Probabilistic Planning
### Value Iteration Algorithm

Value Iteration (VI) is a method of computing an optimal Markov Decison Process (MDP) policy and its value.

#### Usage
```
python3 valueiteration.py navigation_instances\navigation01.net
```

#### Sample output
```
>> Policy
robot-at-x01y01 -> move-north
robot-at-x01y02 -> move-north
robot-at-x01y03 -> move-east
robot-at-x02y01 -> move-west
robot-at-x02y02 -> move-north
robot-at-x02y03 -> move-east
robot-at-x03y01 -> move-west
robot-at-x03y02 -> move-north
robot-at-x03y03 -> move-east
robot-at-x04y01 -> move-west
robot-at-x04y02 -> move-north
robot-at-x04y03 -> move-south
broken-robot -> move-south

>> Time: parsing = 0.0030, solving = 0.1391
```