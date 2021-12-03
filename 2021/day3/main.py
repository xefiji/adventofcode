import csv

def get_input(file = 'input.csv'):
    with open(file, newline='') as csvfile:
        input = []
        reader = csv.reader(csvfile)
        for row in reader:
            input.append(row[0])

    return input

def part1():
    gamma, epsilon = ["0b"], ["0b"]
    for input in to_columns(get_input()):
        most_seen = "1" if input.count(1) >= len(input)/2 else "0"
        gamma.append(most_seen)
        epsilon.append("1" if most_seen == "0" else "0")
    return int("".join(gamma), 2) * int("".join(epsilon), 2)

def part2():
    co2, oxy = get_input(), get_input()

    i = 0
    while len(co2) != 1:
        most_seen = get_most_seen(to_columns(co2), i)
        most_seen = 1 if most_seen == -1 else most_seen
        co2 = list(filter((lambda x: x[i] == str(most_seen)), co2))
        i+=1

    i = 0
    while len(oxy) != 1:
        most_seen = get_most_seen(to_columns(oxy), i, True)
        most_seen = 0 if most_seen == -1 else most_seen
        oxy = list(filter((lambda x: x[i] == str(most_seen)), oxy))
        i+=1

    return int(co2[0], 2) * int(oxy[0], 2)

def to_columns(input):
    output = [[] for x in range(len(input[0]))]
    for row in input:
        for i, bit in enumerate(row):
            output[i].append(int(bit))
    return output

def get_most_seen(columns, offset = 0, reversed = False):
    for i, vals in enumerate(columns):
        if i < offset:
            continue
        ones = vals.count(1)
        zeros = vals.count(0)
        if ones == zeros:
            return -1
        elif ones > zeros:
            return 0 if reversed else 1
        else:
            return 1 if reversed else 0
    return None


print('result of part 1 is {}'.format(part1()))
print('result of part 2 is {}'.format(part2()))