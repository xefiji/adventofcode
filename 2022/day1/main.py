import sys, os

def get_input():
    return [sum(map(int, x.split('\n'))) for x in list(open('input.txt').read().split('\n\n'))]

def part1():
    return max(get_input())    

def part2():    
    return sum(sorted(get_input(), reverse=True)[0:3])

print('result of part 1 is {}'.format(part1()))
print('result of part 2 is {}'.format(part2()))
