with open((__file__.rstrip("8.py")+"8.txt"), 'r') as input_file:
 input = [list(map(int, [*line])) for line in input_file.read().split('\n')]

ans = 0
print(input)
for row in range(len(input)):
    for col in range(len(input[row])):
        curr = input[row][col]
        if all([input[row][c] < curr for c in range(col)]) or all([input[row][c] < curr for c in range(col+1, len(input[row]))]) or all([input[r][col] < curr for r in range(row)]) or all([input[r][col] < curr for r in range(row+1, len(input))]):
            ans += 1

print("Part One : "+ str(ans))

ans = 0

for row in range(len(input)):
    for col in range(len(input[row])):
        k = input[row][col]
        left = right = top = bottom = 0
        for x in range(col-1, -1, -1):
            left += 1
            if input[row][x] >= k:
                break
        for x in range(col+1, len(input[row])):
            right += 1
            if input[row][x] >= k:
                break
        for x in range(row-1, -1, -1):
            top += 1
            if input[x][col] >= k:
                break
        for x in range(row+1, len(input)):
            bottom += 1
            if input[x][col] >= k:
                break
        ans = max(ans, left * right * top * bottom)



print("Part Two : "+ str(ans))
