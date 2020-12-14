import csv, os, sys

def get_input(file = 'input.csv'):
    fileName = "{}/2020/day11/{}".format(os.getcwd(), file)
    input = []
    with open(fileName, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            input.append([c for c in row[0]])            
    return input

def part1():
    input = get_input()    
    size, has_changed = (len(input), len(input[0])), True
    
    while has_changed is True:
        next_input = [['.' for a in range(size[1])] for b in range(size[0])]    
        for i, row in enumerate(input):                
            for j, seat in enumerate(row):
                if seat == "L" and count_occupied_neighboors(input, i, j) == 0:                
                    next_input[i][j] = "#"
                    pass
                elif seat == "#" and count_occupied_neighboors(input, i, j) >=4:
                    next_input[i][j] = "L"
                    pass
                else:
                    next_input[i][j] = seat
        total, has_changed = traverse(input, next_input)            
        input = next_input                    
    
    return total

def traverse(old, new):
    total = 0
    has_changed = False
    for i, row in enumerate(new):
        for j, seat in enumerate(row):
            total += 1 if seat == "#" else 0
            if False == has_changed and seat != old[i][j]:                
                has_changed = True
    
    return total, has_changed

def count_occupied_neighboors(input, y, x):
    count = 0

    top = input[y-1][x] if y-1 > -1 else None      
    top_r = input[y-1][x+1] if y-1 > -1 and x+1 < len(input[y-1]) else None                               
    right = input[y][x+1] if x+1 < len(input[y]) else None
    bottom_r = input[y+1][x+1] if y+1 < len(input) and x+1 < len(input[y]) else None
    bottom = input[y+1][x] if y+1 < len(input) else None
    bottom_l = input[y+1][x-1] if y+1 < len(input) and x-1 > -1 else None
    left = input[y][x-1] if x-1 > -1 else None
    top_l = input[y-1][x-1] if y-1 > -1 and x-1 > -1 else None
        
    count += 1 if top == "#" else 0
    count += 1 if top_r == "#" else 0
    count += 1 if right == "#" else 0
    count += 1 if bottom_r == "#" else 0
    count += 1 if bottom == "#" else 0
    count += 1 if bottom_l == "#" else 0
    count += 1 if left == "#" else 0
    count += 1 if top_l == "#" else 0

    return count    

def part2():
    input = get_input()    
    size, has_changed = (len(input), len(input[0])), True
    while has_changed is True:
        next_input = [['.' for a in range(size[1])] for b in range(size[0])]    
        for i, row in enumerate(input):                
            for j, seat in enumerate(row):
                if seat == "L" and count_occupied_neighboors_2(input, i, j, "L", "#") == 0:                
                    next_input[i][j] = "#"
                    pass
                elif seat == "#" and count_occupied_neighboors_2(input, i, j, "L", "#") >= 5:
                    next_input[i][j] = "L"
                    pass
                else:
                    next_input[i][j] = seat
        total, has_changed = traverse(input, next_input)         
        input = next_input                
        
    return total           

def count_occupied_neighboors_2(input, y, x, old, new):

    count = 0
    top = None
    for i in reversed(range(y)):
        if input[i][x] == old:
            break
        if input[i][x] == new:
            top = input[i][x]
            break

    top_r = None
    tmp = x + 1 
    for i in reversed(range(y)):
        try:            
            if tmp > len(input[i]):
                break
            if input[i][tmp] == old:
                break
            if input[i][tmp] == new:
                top_r = input[i][tmp]
                break
            tmp += 1
        except IndexError:
            break

    right = None    
    for i in range(x+1, len(input[y])):       
        if input[y][i] == old:
            break
        if input[y][i] == new:
            right = input[y][i]
            break

    bottom_r = None
    tmp = x + 1 
    for i in range(y+1, len(input)):        
        try:            
            if tmp > len(input[i]):
                break
            if input[i][tmp] == old:
                break
            if input[i][tmp] == new:
                bottom_r = input[i][tmp]
                break
            tmp += 1
        except IndexError:
            break

    bottom = None
    for i in range(y+1, len(input)):                
        if input[i][x] == old:
            break
        if input[i][x] == new:
            bottom = input[i][x]
            break

    bottom_l = None
    tmp = x - 1 
    for i in range(y+1, len(input)):        
        try:
            if tmp < 0:
                break           
            if input[i][tmp] == old:    
                break
            if input[i][tmp] == new:
                bottom_l = input[i][tmp]
                break
            tmp -= 1
        except IndexError:            
            break

    left = None
    for i in reversed(range(x)):
        if input[y][i] == old:
            break
        if input[y][i] == new:
            left = input[y][i]
            break

    top_l = None
    tmp = x - 1 
    for i in reversed(range(y)):
        try:            
            if tmp < 0:
                break
            if input[i][tmp] == old:
                break
            if input[i][tmp] == new:
                top_l = input[i][tmp]
                break
            tmp -= 1
        except IndexError:
            break    

    res = [count + 1 for seat in [top, top_r, right, bottom_r, bottom, bottom_l, left, top_l] if seat == "#"]    
    return sum(res)


print('result of part 1 is {}'.format(part1()))
print('result of part 2 is {}'.format(part2()))