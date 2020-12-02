import csv

def get_input(file = 'input.csv'):
    input = []
    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            input.append(int(row[0]))
    return input


def part1():
    passed = {}
    for input in get_input():
        try:
            known = passed[input]
            return known * input
        except KeyError:
            sub = 2020 - input
            passed[sub] = input
    return None


def part2():
    input = get_input()        
    for i in input:
        for j in input:
            rest = 2020 - (i + j)
            if rest in input:
                return i * j * rest                
    return None      
                
print('result of part 1 is {}'.format(part1()))
print('result of part 2 is {}'.format(part2()))
