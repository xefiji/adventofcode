import csv, os

def get_input(file = 'input.csv'):
    fileName = "{}/2020/day9/{}".format(os.getcwd(), file)
    input = []
    with open(fileName, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            input.append(int(row[0]))
    return input


def part1():
    plength = 25
    input = get_input()
    multiples = input[0:plength]    
    for i, _ in enumerate(input, start=plength):        
        num = input[i]        
        if False == (True in [(num - m in multiples) for m in multiples if m != num and num/2 != m]):        
            return i, num            
        multiples = input[(i-plength + 1):(i+1)] # make preambule progress
    return None


def part2():    
    input = get_input()
    p = part1()

    index = p[0]
    target = p[1]        
    sub = target

    while True:
        found = []
        iterable = list(reversed(range(index)))
        for i in iterable:        
            sub -= input[i]
            found.append(input[i])
            if sub == 0:
                s = sorted(found)                            
                return s[0] + s[len(s)-1]
            if sub < 0:
                sub = target
                found = []
                index -= 1                
                break            
                
print('result of part 1 is {}'.format(part1()[1]))
print('result of part 2 is {}'.format(part2()))
