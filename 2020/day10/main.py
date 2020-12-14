import csv, os

def get_input(file = 'input.csv'):
    fileName = "{}/2020/day10/{}".format(os.getcwd(), file)
    input = []
    with open(fileName, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            input.append(int(row[0]))
    return input

def part1():     
    input = sorted(get_input())     
    diff1, diff3 = 0, 1
    for i, charger in enumerate(input):
        diff = (charger - input[i-1] if i > 0 else charger)        
        if diff == 3:
            diff3 += 1
        if diff == 1:
            diff1 += 1
    return diff1 * diff3

# too naïve, not working with real puzzle datas :/
# todo nCr
def part2():
    input = get_input()
    input.extend([0, max(input)+3])
    input = sorted(input)    
    t = traverse(input, 1)
    return t

def traverse(input, total):
    for i, _ in enumerate(input):        
        if i == 0 or i == len(input) - 1:
            continue
        if input[i+1] - input[i-1] <= 3:        
            poss = [input[j] for j, elt in enumerate(input) if j != i]          
            newtotal = total + 1            
            total = traverse(poss[i-1:], newtotal)                        
    return total
                


print('result of part 1 is {}'.format(part1()))
print('result of part 2 is {}'.format(part2()))