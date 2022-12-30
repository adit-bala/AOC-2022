import re
import copy
with open((__file__.rstrip("11.py")+"11.txt"), 'r') as input_file:
 input = input_file.read().split('\n\n')

# keep track of monkey: behavior, items, # inspections
ops = {"*" : lambda x : lambda y: x * y, "+": lambda x : lambda y: x + y, "pow" : lambda x: pow(x, 2)}
cyc = {}
mx = 0
# parsing
for line in input:
    m = line.split('\n')
    mx = n = int(m[0].split()[1][:-1])
    itm = list(map(int, (re.findall(r'\d+', m[1]))))
    if "*" in m[2]:
        if m[2].count("old") > 1:
            op = ops.get("pow")
        else:
            op = ops.get("*")(int(m[2][-2:]))
    else:
        op = ops.get("+")(int(m[2][-2:]))
    th = []
    for i in range(3, 6):
        th.append((int(m[i][-2:])))
    cyc[n] = [itm, op, th, 0]
cyc2 = copy.deepcopy(cyc)
# pt1
for _ in range(20):
    for i in range(mx + 1):
        c = cyc.get(i)
        while c[0]:
            itm = c[0].pop(0)
            itm = c[1](itm) // 3
            t = c[2]
            cyc.get(t[1])[0].append(itm) if itm % t[0] == 0 else cyc.get(t[2])[0].append(itm)
            c[3] += 1 

tot = []
for i in range(mx + 1):
    tot += [cyc.get(i)[3]]
    

print("Part One : "+ str((lambda x, y: x * y)(*sorted(tot)[-2:])))
# pt2

mod = 1
for i in range(mx + 1):
    mod *= cyc2.get(i)[2][0]

for _ in range(10000):
    for i in range(mx + 1):
        c = cyc2.get(i)
        while c[0]:
            itm = c[0].pop(0)
            itm = c[1](itm)
            itm %= mod
            t = c[2]
            cyc2.get(t[1])[0].append(itm) if itm % t[0] == 0 else cyc2.get(t[2])[0].append(itm)
            c[3] += 1 

tot = []
for i in range(mx + 1):
    tot += [cyc2.get(i)[3]]
    

print("Part Two : "+ str((lambda x, y: x * y)(*sorted(tot)[-2:])))
