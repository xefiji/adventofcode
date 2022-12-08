import re, sys

def part1():      
    return sum([x for x in get_dirs().values() if x <= 100000])
    
def part2():  
    dirs = get_dirs()
    needed = 30000000 - (70000000 - dirs["/"])
    return min([x for x in dirs.values() if x >= needed])

def get_dirs():
    input = open('input.txt').read().splitlines()  
    dirs = {}
    path = []
    for line in input:
        parts = line.strip().split()
        if parts[1] == "cd":
            if parts[2] == '..':
                path.pop()
            else:
                path.append(parts[2])
        elif parts[1] == "ls":
            continue
        else:
            elt = line.split(' ')
            try:                    
                size = int(elt[0])
                subpath = ""
                for sub in path:
                    subpath += "/" + sub
                    subpath = subpath.replace("///", "/").replace("//", "/")
                    if subpath not in dirs.keys():
                        dirs[subpath] = 0      
                    dirs[subpath] += size
            except:
                pass
    return dirs

print('result of part 1 is {}'.format(part1()))
print('result of part 2 is {}'.format(part2()))
