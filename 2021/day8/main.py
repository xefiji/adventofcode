import math, sys

def part1():
    lines = list(map(lambda x: x.split(' | ')[1].split(' '),open('input.csv').read().split('\n')))
    res = {i: 0 for i in range(9)}
    for line in lines:
        for digit in line:
            res[len(digit)] += 1
    return res[2] + res[3] + res[4] + res[7]

def part2():
    input = list(map(lambda x: x.split(' | '),open('input.csv').read().split('\n')))
    lines = list(map(lambda x:[x[0].split(' '), x[1].split(' ')], input))
    total = 0

    for line in lines:

        # build signals dict indexed by length
        signals = {len(x): [] for x in sorted(line[0], key=len)}
        for signal in line[0]:
            signals[len(signal)].append(signal)

        # indexing function to ease final lookup
        sort_string = lambda x: "".join(sorted(x))

        # build result dict indexed by signal (start with well known)
        res = {
            sort_string(signals[2][0]): 1,
            sort_string(signals[4][0]): 4,
            sort_string(signals[3][0]): 7,
            sort_string(signals[7][0]): 8
        }
        
        # melt function to add mask to digit and return the melting result
        melt = lambda digit, mask: len(list(dict.fromkeys(digit + mask)))

        # melt 6 with 1 and 4 (should be 6, 0 or 9)
        for elt in signals[6]:
            if melt(elt, signals[2][0]) == 7:
                res[sort_string(elt)] = 6
                continue

            if melt(elt, signals[4][0]) == 7:
                res[sort_string(elt)] = 0
                continue

            res[sort_string(elt)] = 9

        # melt 5 with 4 and 7 (should be 2, 5 or 3)
        for elt in signals[5]:
            if melt(elt, signals[4][0]) == 7:
                res[sort_string(elt)] = 2
                continue

            if melt(elt, signals[3][0]) == 6:
                res[sort_string(elt)] = 5
                continue

            res[sort_string(elt)] = 3

        total += int("".join([str(res[sort_string(digit)]) for digit in line[1]]))
    
    return total

print('result of part 1 is {}'.format(part1()))
print('result of part 2 is {}'.format(part2()))