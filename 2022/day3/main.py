import sys, os

def convert(x):
    return ord(x)-96 if x.islower() else ord(x)-38

def part1():
    rucksacks = [ [x[0:((len(x)//2))], x[((len(x)//2)):]] for x in list(open('input.txt').read().splitlines())] 
    dup = [list(set(rucksack[0]) & set(rucksack[1])) for rucksack in rucksacks]

    convert = lambda x : ord(x)-96 if x.islower() else ord(x)-38
    return sum([sum(y) for y in [list(map(convert, x)) for x in dup]])

def part2():    
    rucksacks = [x for x in list(open('input.txt').read().splitlines())]
    groups = []
    current = []
    for i, ruckstack in enumerate(rucksacks):
        current.append(ruckstack)
        if (i+1)%3 == 0:
            groups.append(current)
            current = []

    return sum([convert(list(set(group[0]) & set(group[1]) & set(group[2]))[0]) for group in groups])

print('result of part 1 is {}'.format(part1()))
print('result of part 2 is {}'.format(part2()))
