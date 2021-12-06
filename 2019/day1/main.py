import math

def part1():
    apply = lambda x: math.floor(x/3) - 2
    return sum(list(map(apply, map(int,open("input.csv").read().splitlines()))))

def part2():
    def apply(x):
        compute = lambda x: math.floor(x/3) - 2
        measures, fuel = [], compute(x)
        while fuel > 0:
            measures.append(fuel)
            fuel = compute(fuel)
        return sum(measures)
    return sum(list(map(apply, map(int,open("input.csv").read().splitlines()))))

print('result of part 1 is {}'.format(part1()))
print('result of part 2 is {}'.format(part2()))
