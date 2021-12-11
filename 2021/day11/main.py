def part1():
    grid, total = get_grid(), 0
    for _ in range(100):
        grid, total = round_r(incr(grid), total)
    return total

def part2():
    grid, step = get_grid(), 1
    while not is_synced(round_r(incr(grid))[0]):
        step += 1
    return step

def get_grid():
    to_ints = lambda x: [int(elt) for elt in x]
    return list(map(to_ints, map(list, open('input.csv').read().split("\n"))))

def is_synced(grid):
    return all([line.count(0) == len(line) for line in grid])

def incr(grid):
    for y, line in enumerate(grid):
        for x, energy in enumerate(line):
            if energy < 10:
                grid[y][x] += 1
    return grid
    
def round_r(grid, total = 0):
    flashed = []
    for y, line in enumerate(grid):
        for x, energy in enumerate(line):
            if energy == 10: # incr energy of all neighboors
                if y-1 >= 0:
                    grid[y-1][x] += 1 if grid[y-1][x] < 10 else 0
                if y-1 >= 0 and x+1 < len(line):
                    grid[y-1][x+1] += 1  if grid[y-1][x+1] < 10 else 0
                if x+1 < len(line):
                    grid[y][x+1] += 1 if grid[y][x+1] < 10 else 0
                if y+1 < len(grid) and x+1 < len(line):
                    grid[y+1][x+1] += 1 if grid[y+1][x+1] < 10 else 0
                if y+1 < len(grid):
                    grid[y+1][x] += 1 if grid[y+1][x] < 10 else 0
                if y+1 < len(grid) and x-1 >= 0:
                    grid[y+1][x-1] += 1 if grid[y+1][x-1] < 10 else 0
                if x-1 >= 0:
                    grid[y][x-1] += 1 if grid[y][x-1] < 10 else 0
                if y-1 >= 0 and x-1 >=0:
                    grid[y-1][x-1] += 1 if grid[y-1][x-1] < 10 else 0

                flashed.append([x, y]) # keep track of flashed
                grid[y][x] = 0 # reset current
                grid, total = round_r(grid, total) # recursive call
    
    for f in flashed:
        grid[f[1]][f[0]] = 0 # reset flashed

    return grid, (total + len(flashed))

print('result of part 1 is {}'.format(part1()))
print('result of part 2 is {}'.format(part2()))