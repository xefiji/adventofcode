import sys

def part1():
    change = lambda x, i: 12 if i == 1 else 2 if i == 2 else x
    lines = [change(x, i) for i, x in enumerate(list(map(int,open("input.csv").read().split(","))))]
    pos = 0
    while True:
        if lines[pos] == 99:
            return lines[0]
        elif lines[pos] == 2:
            lines[lines[pos+3]] = lines[lines[pos+1]] * lines[lines[pos+2]]
        elif lines[pos] == 1:
            lines[lines[pos+3]] = lines[lines[pos+1]] + lines[lines[pos+2]]
        pos +=4    

def part2():
    return None

print('result of part 1 is {}'.format(part1()))
print('result of part 2 is {}'.format(part2()))
