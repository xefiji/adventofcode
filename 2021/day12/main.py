def part1():    
    return len(get_paths(1))

def part2():
    return len(get_paths(2))

def get_paths(part):
    tmp = list(map(lambda x: x.split('-'), open('input.csv').read().split("\n")))
    # permutations
    lines = list([x for l in (list(map(lambda x:[[x[0], x[1]], [x[1], x[0]]], tmp))) for x in l])
    # remove duplicates and start/end from 
    lines = list(filter((lambda x: x[1] != "start" and x[0] != "end"), filter(lambda x:lines.count(x) < 2, lines)))

    # initiate paths with starts nodes and filter them
    paths = []
    for l in lines:
        if l[0] == "start":
            paths.append([l[0], l[1]])

    lines = list(filter((lambda x: x[0] != "start" and x[1] != "start"), lines))

    while any([x.count("end") == 0 for x in paths]):
        new_paths = []
        for path in paths:
            if path.count("end") > 0:
                new_paths.append(path)
                continue

            for line in lines:
                if line[0] == path[-1]: # line matches with path end
                    if part == 1 and line[1].islower() and line[1] in path: # filter small caves already passed
                        continue
                    elif part == 2 and line[1].islower() and path.count(line[1]) > 0:
                            if path.count(line[1]) > 1 or any(filter(lambda x: x != line[1] and x.islower() and path.count(x) > 1, path)):
                                continue
                            
                    tmp = path.copy()
                    tmp.append(line[1])
                    new_paths.append(tmp)

        paths = new_paths.copy()
    return paths

print('result of part 1 is {}'.format(part1()))
print('result of part 2 is {}'.format(part2()))



