with open((__file__.rstrip("1.py")+"1.txt"), 'r') as input_file:
 input = input_file.read().split('\n')

elfs = [0]
index = 0
for line in input:
    if line:
        elfs[index] += (int(line))
    else:
        elfs.append(0)
        index += 1

max_elf = max(elfs)

print("Part One : "+ str(max_elf))

elfs.sort()
top_three = sum(elfs[-3:])

print("Part Two : "+ str(top_three))