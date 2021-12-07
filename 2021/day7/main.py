import math

def part1():
    positions = sorted(list(map(int, open('input.csv').read().split(','))))
    return sum(list(map(lambda x: abs(x - positions[math.floor(len(positions)/2)-1]), positions)))

def part2():
    positions = sorted(list(map(int, open('input.csv').read().split(','))))
    avg = math.floor(sum(positions)/(len(positions)))
    compute = lambda pos:(abs(avg-pos)*(abs(avg-pos)+1))//2
    return sum(list(map(compute, positions)))

print('result of part 1 is {}'.format(part1()))
print('result of part 2 is {}'.format(part2()))