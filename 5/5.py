with open((__file__.rstrip("5.py")+"5.txt"), 'r') as input_file:
 input = input_file.read().split('\n')

boxes = []
num = 9
inst = []
stacks = []

for line in input:
    # boxes   
    if line and line[0] == '[':
        boxes.append([line[i:i+3] for i in range(0, len(line), 4)])
    # instructions
    if line and line[0] == 'm':
        amt = int(line[5:line.index('from')])
        start = int(line[line.index('from')+len('from'):line.index('to')])
        end = int(line[line.index('to') + len('to'):])
        inst.append((amt, start - 1, end - 1))

for box in range(num):
    stacks.append([row[box] for row in boxes if not row[box].isspace()][::-1])
    
for move in inst:
    for n in range(move[0]):
        stacks[move[2]].append(stacks[move[1]].pop())

message = ""
for stack in stacks:
    last = stack[len(stack)-1]
    message += (last[last.index('[')+1:last.index(']')])


print("Part One : "+ str(message))

crane = []

for box in range(num):
    crane.append([row[box] for row in boxes if not row[box].isspace()][::-1])
 
for move in inst:
    start, end, take = crane[move[1]], crane[move[2]], move[0]
    #print('\n', start, end, take, '\n')
    rm = start[-take:]
    crane[move[1]] = start[:-take]
    end.extend(rm)
    #print(start, end)

new = ""

for col in crane:
    last = col[len(col)-1]
    new  += (last[last.index('[')+1:last.index(']')])

print("Part Two : "+ str(new))
