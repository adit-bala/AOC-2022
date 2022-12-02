with open((__file__.rstrip("2.py")+"2.txt"), 'r') as input_file:
 input = input_file.read().split('\n')

scores = {'A': 1, 'B': 2, 'C':3, 'X': 1, 'Y': 2, 'Z': 3}
curr = 0

for round in input:
    opp, me = scores.get(round[0]), scores.get(round[2])
    if opp - me == 0:
        curr += 3 
    elif opp - me == -1 or opp - me == 2:
        curr += 6
    curr += me

print("Part One : "+ str(curr))

new_scores = {'A': [3, 1, 2], 'B': [1, 2, 3], 'C': [2, 3, 1], 'X': (0, 0), 'Y': (1, 3), 'Z': (2, 6)}
correct = 0

for round in input:
    opp, me = new_scores.get(round[0]), new_scores.get(round[2])
    correct += opp[me[0]] + me[1]

print("Part Two : "+ str(correct))
