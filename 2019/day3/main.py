import sys, os

def conv(x):
    return (',').join([str(y) for y in x])

def process(wire, waypoints, detect = False):
    coords = [0,0]
    collisions = []
    i = 0
    for instruction in wire:
        dir = instruction[0]
        move = int(instruction[1:])

        x = coords[0]
        y = coords[1]
    
        if dir == "R":
            for x in list(range(x+1, move+x+1)):
                if detect:
                    if waypoints.get(conv([x, y])):
                        collisions.append([x, y])
                else:
                    i+=1
                    waypoints[conv([x, y])] = i
        if dir == "L":
            for x in list(range(x-1, x-move-1, -1)):
                if detect:
                    if waypoints.get(conv([x, y])):
                        collisions.append([x, y])
                else:
                    i+=1
                    waypoints[conv([x, y])] = i
        if dir == "U":
            for y in list(range(y+1, move+y+1)):
                if detect:
                    if waypoints.get(conv([x, y])):
                        collisions.append([x, y])
                else:
                    i+=1
                    waypoints[conv([x, y])] = i
        if dir == "D":
            for y in list(range(y-1, y-move-1, -1)):
                if detect:
                    if waypoints.get(conv([x, y])):
                        collisions.append([x, y])
                else:
                    i+=1
                    waypoints[conv([x, y])] = i
        coords = [x, y]

    return [waypoints, collisions]

def part1():
    wires = list(map(lambda x:x.split(','), list(open('input.txt').read().splitlines())))
    _, collisions = process(wires[1], process(wires[0], {}, False)[0], True)
    return min(list(map(lambda x: sum([abs(y) for y in x]), [x for x in collisions])))

def part2():
    wires = list(map(lambda x:x.split(','), list(open('input.txt').read().splitlines())))
    wire1 = process(wires[0], {}, False)
    wire2 = process(wires[1], {}, False)
    
    return min(list([wire1[0][x] + wire2[0][x] for x in [conv(x) for x in process(wires[1], wire1[0], True)[1]]]))

print('result of part 1 is {}'.format(part1()))
print('result of part 2 is {}'.format(part2()))
