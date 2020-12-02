import csv

def get_input(file = 'input.csv'):
    input = []
    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            input.append(row[0])
    return input

def parse(input):
    parts = input.split(':')
    rule = parts[0].strip()
    pwd = parts[1].strip()

    rl = rule.split(' ')
    rule = rl[0].strip()
    letter = rl[1].strip()

    minmax = rule.split('-')
    min = int(minmax[0].strip())
    max = int(minmax[1].strip())

    return min, max, letter, pwd


def part1():    
    valids = 0
    for input in get_input():    
        min, max, letter, pwd = parse(input)
        occ = pwd.count(letter)
        if occ >= min and occ <= max:
            valids += 1
    return valids

def part2():
    valids = 0
    for input in get_input():        
        pos1, pos2, letter, pwd = parse(input)        
        valids += 1 if (pwd[pos1-1] == letter) != (pwd[pos2-1] == letter) else 0    
    return valids

    
print('result of part 1 is {}'.format(part1()))
print('result of part 2 is {}'.format(part2()))
