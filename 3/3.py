with open((__file__.rstrip("3.py")+"3.txt"), 'r') as input_file:
 input = input_file.read().split('\n')

curr = 0

for sack in input:
    middle = len(sack) // 2
    first, second = sack[:middle], sack[middle:]
    common = "".join(set(first).intersection(second))
    print(common, ord(common))
    if ord(common) > 90:
        curr += ord(common) - 96
    else:
        curr += ord(common) - 38

print("Part One : "+ str(curr))

group = 0
for a, b, c in zip(*[iter(input)]*3):
    common = "".join(set(a) & set(b) & set(c))
    print(common, ord(common))
    if ord(common) > 90:
        group += ord(common) - 96
    else:
        group += ord(common) - 38
 
print("Part Two : "+ str(group))
