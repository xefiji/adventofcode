import sys, os

def get_pairs():
    pairs = [x.split(',') for x in list(open('input.txt').read().splitlines())] 
    return [[list(map(int, pair[0].split('-'))), list(map(int, pair[1].split('-')))] for pair in pairs]

def part1():
    pairs = get_pairs()
    return len(list(filter(lambda x: [min([x[0][0], x[1][0]]), max([x[0][1], x[1][1]])] in x, pairs)))

def part2():    
    pairs = get_pairs()
    i = 0
    for pair in pairs:
        check_overlap = lambda point, pair: point in range(pair[0], pair[1]+1)
        if check_overlap(pair[0][0], pair[1]) or \
                check_overlap(pair[0][1], pair[1]) or \
                check_overlap(pair[1][0], pair[0]) or \
                check_overlap(pair[1][1], pair[0]):
            i += 1            
    return i

print('result of part 1 is {}'.format(part1()))
print('result of part 2 is {}'.format(part2()))
