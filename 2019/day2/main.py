import sys

def part1():
    return compute(12, 2)

def part2():
    for a in range(100):
        for b in range(100):
            if compute(a, b) == 19690720:
                return 100*a+b


def compute(a, b):
    change = lambda x, i: a if i == 1 else b if i == 2 else x
    int_code = [change(x, i) for i, x in enumerate(list(map(int,open("input.csv").read().split(","))))]
    pos = 0    
    while True:        
        if pos >= len(int_code) or int_code[pos] == 99:            
            return int_code[0]            
        elif int_code[pos] == 2:
            int_code[int_code[pos+3]] = int_code[int_code[pos+1]] * int_code[int_code[pos+2]]
        elif int_code[pos] == 1:
            int_code[int_code[pos+3]] = int_code[int_code[pos+1]] + int_code[int_code[pos+2]]
        pos +=4


print('result of part 1 is {}'.format(part1()))
print('result of part 2 is {}'.format(part2()))
