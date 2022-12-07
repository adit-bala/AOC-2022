import re
import string

with open((__file__.rstrip("7.py")+"7.txt"), 'r') as input_file:
 input = input_file.read().split('\n')

class Dir:

    total = [] 

    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.contents = {}
        self.size = 0
        Dir.total.append(self)

    def add_item(self, line):
        if "dir" in line:
            self.contents[line[4:]] = Dir(line[4:], self)
        elif line:
            fsize = int(re.findall(r'\d+', line)[0])
            self.size += fsize
            self.update_parent(fsize)

    def update_parent(self, size):
        curr = self.parent
        while curr:
            curr.size += size
            curr = curr.parent

parent = None
root = None
for cmd in range(len(input)):
    if "$ cd" in input[cmd]:
        if ".." in input[cmd]:
            parent = parent.parent
            continue
        if not root:
            parent = Dir(input[cmd][5:], parent)
            root = parent
        else:
            parent = parent.contents[input[cmd][5:]]   
    elif "$" not in input[cmd]:
        parent.add_item(input[cmd])

curr = 0
for size in Dir.total:
    if size.size <= 100000:
        curr += size.size
print("Part One : "+ str(curr))

clear = 30000000 - (70000000 - root.size)
amt = min([size.size for size in Dir.total if size.size >= clear])

print("Part Two : "+ str(amt))
