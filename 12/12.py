with open((__file__.rstrip("12.py")+"12.txt"), 'r') as input_file:
 input = input_file.read().split('\n')[:-1]

m = []
sx = sy = ex = ey = 0
s = e = 0
for line in input:
    if "S" in line: 
        sx = len(m)
        sy = line.index("S")
        line = line.replace("S", "a")
    if "E" in line:
        ex = len(m)
        ey = line.index("E")
        line = line.replace("E", "z")
    m.append(list(line))


# pt1 -> bfs
v = {(sx, sy)}
q = [] 
sol = 0
q.append((0, sx, sy))

while q:
    d, cx, cy = q.pop(0)
    for ax, ay in [(cx + 1, cy), (cx - 1, cy), (cx, cy + 1), (cx, cy - 1)]:
        if ax < 0 or ay < 0 or ax >= len(m) or ay >= len(m[0]):
            continue
        if (ax, ay) in v:
            continue
        if ord(m[ax][ay]) - ord(m[cx][cy]) > 1:
            continue
        if ax == ex and ay == ey:
            sol = d + 1
            break
        v.add((ax, ay))
        q.append((d + 1, ax, ay))


print("Part One : "+ str(sol))

v = {(ex, ey)}
q = [] 
sol = 0
q.append((0, ex, ey))

while q:
    d, cx, cy = q.pop(0)
    for ax, ay in [(cx + 1, cy), (cx - 1, cy), (cx, cy + 1), (cx, cy - 1)]:
        if ax < 0 or ay < 0 or ax >= len(m) or ay >= len(m[0]):
            continue
        if (ax, ay) in v:
            continue
        if ord(m[ax][ay]) - ord(m[cx][cy]) < -1:
            continue
        if m[ax][ay] == "a":
            print(sol)
            sol = d + 1
            break
        v.add((ax, ay))
        q.append((d + 1, ax, ay))




print("Part Two : "+ str(sol))
