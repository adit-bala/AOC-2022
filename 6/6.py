with open((__file__.rstrip("6.py")+"6.txt"), 'r') as input_file:
 input = input_file.read()

index = 0

for i in range(len(input) - 4):
    print(input[i: i + 4])
    if len(set(input[i: i + 4])) == 4:
            index = i + 4
            break

print("Part One : "+ str(index))

new = 0

for i in range(len(input) - 14):
    print(input[i: i + 14])
    if len(set(input[i: i + 14])) == 14:
            new = i + 14
            break

print("Part Two : "+ str(new))
