import math

with open((__file__.rstrip("9.py")+"9.txt"), 'r') as input_file:
    input = input_file.read().split('\n')

def dist(hx, hy, tx, ty):
    return int(math.dist([hx, hy], [tx, ty]))
def cd(hx, hy, tx, ty):
    return True if abs(hx - tx) == abs(hy - ty) else False
def pg(grid):
    for i in grid:
        print(i)
    print('\n')
 
 
grid = [[0, 0], [0, 0]]
hx = tx = 1
hy = ty = 0
diag = False
for line in input:
    mv, num = line.split()
    if mv == 'R':
        for i in range(int(num)):
            if hy + 1 == len(grid[hx]):
                for i in grid:
                    i.append(0)
            hy += 1
            if diag and dist(hx, hy, tx, ty) > 1:
                tx = hx
                ty = hy - 1
            elif dist(hx, hy, tx, ty) > 1:
                ty += 1
            grid[tx][ty] = 1
            diag = cd(hx, hy, tx, ty)
    if mv == 'L':
        for i in range(int(num)):
            if hy - 1 < 0:
                for i in grid:
                    i.insert(0, 0)
                hy += 1
                ty += 1
            hy -= 1
            if diag and dist(hx, hy, tx, ty) > 1:
                tx = hx
                ty = hy + 1
            elif dist(hx, hy, tx, ty) > 1:
                ty -= 1
            grid[tx][ty] = 1
            diag = cd(hx, hy, tx, ty)
    if mv == 'D':
        for i in range(int(num)):
            if hx + 1 == len(grid):
                grid.append([0 for i in range(len(grid[hx]))])
            hx += 1
            if diag and dist(hx, hy, tx, ty) > 1:
                tx = hx - 1
                ty = hy
            elif dist(hx, hy, tx, ty) > 1:
                tx += 1
            grid[tx][ty] = 1
            diag = cd(hx, hy, tx, ty)
    if mv == 'U':
        for i in range(int(num)):
            if hx - 1 < 0:
                grid.insert(0, [0 for i in range(len(grid[hx]))])
                hx += 1
                tx += 1
            hx -= 1
            if diag and dist(hx, hy, tx, ty) > 1:
                tx = hx + 1
                ty = hy
            elif dist(hx, hy, tx, ty) > 1:
                tx -= 1
            grid[tx][ty] = 1
            diag = cd(hx, hy, tx, ty)

total = sum(row.count(1) for row in grid)

print("Part One : "+ str(total))

v = set([(0, 0)])

R = [[0, 0] for _ in range(10)]

for line in input:
    x, y = line.split()
    y = int(y)

    for _ in range(y):
        dx = 1 if x == "R" else -1 if x == "L" else 0
        dy = 1 if x == "U" else -1 if x == "D" else 0

        R[0][0] += dx
        R[0][1] += dy

        for i in range(9):
            H = R[i]
            T = R[i + 1]

            _x = H[0] - T[0]
            _y = H[1] - T[1]

            if abs(_x) > 1 or abs(_y) > 1:
                if _x == 0:
                    T[1] += _y // 2
                elif _y == 0:
                    T[0] += _x // 2
                else:
                    T[0] += 1 if _x > 0 else -1
                    T[1] += 1 if _y > 0 else -1

        v.add(tuple(R[-1]))

print("Part Two : "+ str(len(v)))
