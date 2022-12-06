import re, sys

def part1():
    return check(4)

def part2():    
    return check(14)

def check(num):
    data = open('input.txt').read()
    passed = []
    for i, c in enumerate(data):
        if i >= num :
            if len(passed) == len(set(passed)):
                return i
            passed = passed[1:]
        passed.append(c)
    return None


print('result of part 1 is {}'.format(part1()))
print('result of part 2 is {}'.format(part2()))
