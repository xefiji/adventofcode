from functools import reduce

# easy
def part1():
    lines = list(map(list, open('input.csv').read().split("\n")))
    points = list(map(lambda x: x["point"], get_low_points(lines)))
    return sum(list(map(lambda x: x + 1, points)))

# easy but too much code below :(
def part2():
    lines = list(map(list, open('input.csv').read().split("\n")))
    res = []
    for low_point in get_low_points(lines):
        res.append(roam(lines, low_point["x"], low_point["y"], 1))
    res.sort()
    return reduce(lambda x, y: x * y, res[-3:])

# depth first recursive with accumulator
def roam(lines, x, y, acc):
    lines[y][x] = -1 # flag the ones passed
    for neighboor in get_neighboors(lines, x, y):
        if neighboor is None:
            continue
        neighboor_val = lines[neighboor["y"]][neighboor["x"]]
        if  neighboor_val != -1 and neighboor_val != "9":
            acc += 1
            acc = roam(lines, neighboor["x"], neighboor["y"], acc)
    return acc

# at least it's reused...
def get_neighboors(lines, x, y):
    up = int(lines[y-1][x]) if y > 0 else None
    right = int(lines[y][x+1]) if x < len(lines[y])-1 else None
    down = int(lines[y+1][x]) if y < len(lines)-1 else None
    left = int(lines[y][x-1]) if x > 0 else None

    return [
        {"x": x, "y": y-1, "point": up} if up is not None else None, 
        {"x": x+1, "y": y, "point": right} if right is not None else None,
        {"x": x, "y": y+1, "point": down} if down is not None else None,
        {"x": x-1, "y": y, "point": left} if left is not None else None
    ]

# at least it's reused...
def get_low_points(lines):
    low_points = []
    for y, line in enumerate(lines):
        for x, point in enumerate(list(map(int, line))):    
            neighboors = list(get_neighboors(lines, x, y))
            vals = list(map(lambda x: x['point'], filter(lambda x: x is not None, neighboors)))
            if point < min(vals):
                low_points.append({"x": x, "y": y, "point": point})
    return low_points

print('result of part 1 is {}'.format(part1()))
print('result of part 2 is {}'.format(part2()))