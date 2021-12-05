def part1():
    lines = list(map(lambda line: line.split(' -> '), open('input.csv').read().split('\n')))
    filter_diags = lambda line: (line[0][0] == line[1][0] or line[0][1] == line[1][1])
    all_coords = list(filter(filter_diags, map(parse_coords, lines)))
    return get_duplicates(all_coords)

def part2():
    lines = list(map(lambda line: line.split(' -> '), open('input.csv').read().split('\n')))
    all_coords = list(map(parse_coords, lines))
    return get_duplicates(all_coords)

def parse_coords(line):
    return list(map(lambda coord: [int(coord[0]), int(coord[1])], [line[0].split(','), line[1].split(',')]))

def generate_wind_path(coords_set):
    path = []
    if coords_set[0][0] == coords_set[1][0]:
        x = coords_set[0][0]
        for i in range(coords_set[0][1], coords_set[1][1], (-1 if coords_set[0][1] > coords_set[1][1] else 1)):
            path.append([x, i])
    elif coords_set[0][1] == coords_set[1][1]:
        y = coords_set[0][1]
        for i in range(coords_set[0][0], coords_set[1][0], (-1 if coords_set[0][0] > coords_set[1][0] else 1)):
            path.append([i, y])
    else:
        current = coords_set[0]
        while current != coords_set[1]:
            path.append(current)            
            x = current[0] - 1 if current[0] > coords_set[1][0] else current[0] + 1
            y = current[1] - 1 if current[1] > coords_set[1][1] else current[1] + 1
            current = [x, y]
    path.append(coords_set[1])
    return path


def get_duplicates(all_coords):
    passed, duplicates = {}, 0
    for coords in all_coords:
        for coord in generate_wind_path(coords):
            key = "{},{}".format(coord[0], coord[1])
            if key not in passed:
                passed[key] = 0
            else:
                passed[key] += 1
                duplicates += 1 if passed[key] < 2 else 0
    return duplicates

print('result of part 1 is {}'.format(part1()))
print('result of part 2 is {}'.format(part2()))