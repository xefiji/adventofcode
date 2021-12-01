import csv, sys

def get_input(file = 'input.csv'):
    input = []
    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            input.append(int(row[0]))
    return input


def part1():
    last, count = None, 0
    for input in get_input():
        if last is not None and input > last:
            count += 1
        last = input
    return count


def part2(input = get_input(), last_window_size = 0, total = 0):
    if len(input) <= 3:
        return total + 1 if sum(input) > last_window_size else total
    
    current_window = []
    for current in input:
        current_window.append(current)
        if len(current_window) == 3:
            total += 1 if last_window_size > 0 and sum(current_window) > last_window_size else 0
            return part2(input[1:], sum(current_window), total)

    return None      

sys.setrecursionlimit(3000)
print('result of part 1 is {}'.format(part1()))
print('result of part 2 is {}'.format(part2()))
