with open((__file__.rstrip("4.py")+"4.txt"), 'r') as input_file:
    input = [item.split(',') for item in input_file.read().split('\n')]

curr = 0

for pair in input:
    pairs = [list(map(int, item.split('-'))) for item in pair]
    x1, x2, y1, y2 = pairs[0][0], pairs[1][0], pairs[0][1], pairs[1][1]
    if (x1 <= x2 and y1 >= y2) or (x1 >= x2 and y1 <= y2):
        curr += 1

print("Part One : "+ str(curr))

over = 0

for pair in input:
    pairs = [list(map(int, item.split('-'))) for item in pair]
    x1, x2, y1, y2 = pairs[0][0], pairs[1][0], pairs[0][1], pairs[1][1]
    if x1 <= y2 and y1 >= x2:
        over += 1

print("Part Two : "+ str(over))
