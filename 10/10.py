with open((__file__.rstrip("10.py")+"10.txt"), 'r') as input_file:
    input = input_file.read().split('\n')[:-1]

total = c = 0
X = 1
i = [0]
num = 240
for line in input:
    # begin cycle
    c += 1
    # during cycle
    if line[0] == 'n':
        i += [0]
    else:
        add = int(line.split()[1])
        i += [0, add]

# for pt2
v2 = i[:]

# after cycle
for n in range(1, num + 1):
    v = i.pop(0) 
    if v != 0:
        X += v 
    if (n - 20) % 40 == 0:
        total += X * n


print("Part One : "+ str(total))
d = []
r = 1
l = ""
for n in range(num):
    # restarting line
    if n != 0 and n % 40 == 0:
        d.append(l)
        l = ""
    # begin cycle
    v = v2.pop(0)
    if v != 0:
        r += v
    # during cycle
    if n % 40 in [r - 1, r, r + 1]:
        l += "#"
    else: 
        l += "."

for line in d:
    print(line)


print("Part Two : "+ str("ECZUZALR"))
