import sys, os

def part1():
    return process(lambda x: x >= 2)    

def part2():
    return process(lambda x: x == 2)    

def process(condition):
    def process_number(num):
        increases, consecutives= True, {}        
        for pos, n in enumerate(str(num)):
            try:
                consecutives[n] += 1
            except KeyError:
                consecutives[n] = 1
            if pos > 0 and int(str(num)[pos-1]) > int(n):
                increases = False
        return [num, consecutives, increases]        

    min, max = [int(x) for x in list(open('input.txt').read().split('-'))]
    results = 0    
    for i in range(min, max+1):
        _, consecutives, increases = process_number(i)        
        results += 1 if (increases and len(list([x for x in consecutives.values() if condition(x)])) > 0) else 0
            
    return results

print('result of part 1 is {}'.format(part1()))
print('result of part 2 is {}'.format(part2()))
