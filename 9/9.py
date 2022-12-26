import math

with open((__file__.rstrip("9.py")+"9test.txt"), 'r') as input_file:
    input = input_file.read().split('\n')[:-1]

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

grid = [[0, 0], [0, 0]]
rope = [[[1, 0], False, i - 1 if i - 1 >= 0 else None] for i in range(10)]
def m(px, py, cx, cy, mv, num, diag, n):
    if mv == 'R':
        for i in range(int(num)):
            if py + 1 == len(grid[px]):
                for i in grid:
                    i.append(0)
            py += 1
            if diag and dist(px, py, cx, cy) > 1:
                cx = px
                cy = py - 1
            elif dist(px, py, cx, cy) > 1:
                cy += 1
            if n:
                grid[cx][cy] = 1
            diag = cd(px, py, cx, cy)
    if mv == 'L':
        for i in range(int(num)):
            if py - 1 < 0:
                for i in grid:
                    i.insert(0, 0)
                py += 1
                cy += 1
            py -= 1
            if diag and dist(px, py, cx, cy) > 1:
                cx = px
                cy = py + 1
            elif dist(px, py, cx, cy) > 1:
                cy -= 1
            if n:
                grid[cx][cy] = 1
            diag = cd(px, py, cx, cy)
    if mv == 'D':
        for i in range(int(num)):
            if px + 1 == len(grid):
                grid.append([0 for i in range(len(grid[px]))])
            px += 1
            if diag and dist(px, py, cx, cy) > 1:
                cx = px - 1
                cy = py
            elif dist(px, py, cx, cy) > 1:
                cx += 1
            if n:
                grid[cx][cy] = 1
            diag = cd(px, py, cx, cy)
    if mv == 'U':
        for i in range(int(num)):
            if px - 1 < 0:
                grid.insert(0, [0 for i in range(len(grid[px]))])
                px += 1
                cx += 1
            px -= 1
            if diag and dist(px, py, cx, cy) > 1:
                cx = px + 1
                cy = py
            elif dist(px, py, cx, cy) > 1:
                cx -= 1
            if n:
                grid[cx][cy] = 1
            diag = cd(px, py, cx, cy)
    return (px, py, cx, cy, diag)

for line in input:
    mv, num = line.split()
    for i in range(1, len(rope)):
        parent = rope[rope[i][2]]
        px, py = parent[0]
        cx, cy = rope[i][0]
        n = True if i == len(rope)-1 else False
        print(n)
        res = m(px, py, cx, cy, mv, num, rope[i][1], n)
        rope[rope[i][2]][0] = [res[0], res[1]]
        rope[i][0] = [res[2], res[3]]
        rope[i][1] = res[4]



total = sum(row.count(1) for row in grid)

print("Part Two : "+ str(total))
