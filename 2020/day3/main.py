import csv

def get_input(file = 'input.csv'):
    input = []
    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            input.append(list(row[0]))
    return input


def part1(right, down):
    input = get_input()    
    x, y, sum = 0, 0, 0     
    while y < len(input):
        row = input[y]
        if y != 0:
            x += right
            x = x - len(row) if x >= len(row) else x  
            sum = sum + 1 if row[x] == "#" else sum       
        y += down
    return sum

def part2():    
    res = 1
    for case in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        res = res * part1(case[0], case[1])
    return res
        
                
print('result of part 1 is {}'.format(part1(3, 1)))
print('result of part 2 is {}'.format(part2()))
