import csv

def get_input(file = 'input.csv'):
    input = []
    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            input.append(row[0].split(" "))
    return input


def part1():
    coords = [0, 0]
    apply = (lambda pos, val: [coords[pos] + val if pos == 0 else coords[0], coords[pos] + val if pos == 1 else coords[1]])
    dirs = {"forward": lambda val: apply(0, val), "up": lambda val: apply(1, -val), "down": lambda val: apply(1, val)}
    for instruction in get_input():
        coords = dirs[instruction[0]](int(instruction[1]))
    return coords[0] * coords[1]

def part2():
    coords = [0, 0, 0]
    def apply(direction, val, coords):
        if direction == "forward":
            coords[0] += int(val)
            coords[1] += int(val) * coords[2]
            return coords
        
        if direction == "up":
            coords[2] -= int(val)
            return coords

        if direction == "down":
            coords[2] += int(val)
            return coords

    for instruction in get_input():
        coords = apply(instruction[0], instruction[1], coords)
    return coords[0] * coords[1]

print('result of part 1 is {}'.format(part1()))
print('result of part 2 is {}'.format(part2()))
