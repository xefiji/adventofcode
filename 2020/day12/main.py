import csv, os, sys, functools

def get_input(file = 'input.csv'):
    fileName = "{}/2020/day12/{}".format(os.getcwd(), file)
    input = []
    with open(fileName, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            input.append(row[0])            
    return input

compass = {
    "N": {90: "E", 180: "S", 270: "W"},
    "S": {90: "W", 180: "N", 270: "E"},
    "E": {90: "S", 180: "W", 270: "N"},
    "W": {90: "N", 180: "E", 270: "S"},
}

def part1():
    input = get_input()
    pos = (0, 0) # x, y
    cap = "E"

    for instruction in input:
        dir, val = instruction[:1], int(instruction[1:])        
        if dir == "N" or (dir == "F" and cap == "N"):
            pos = (pos[0], pos[1] + val)
        elif dir == "S" or (dir == "F" and cap == "S"):
            pos = (pos[0], pos[1] - val)
        elif dir == "E" or (dir == "F" and cap == "E"):
            pos = (pos[0] + val, pos[1])
        elif dir == "W" or (dir == "F" and cap == "W"):
            pos = (pos[0] - val, pos[1])
        elif dir == "L":
            cap = compass[cap][(360-val)]
        elif dir == "R":
            cap = compass[cap][val]        

    return abs(pos[0]) + abs(pos[1])


def part2():        
    input = get_input()

    wpt = {'N': 1, 'S': 0, 'E': 10, 'W': 0}
    pos = {'N': 0, 'S': 0, 'E': 0, 'W': 0}

    for instruction in input:
        dir, val = instruction[:1], int(instruction[1:])   
        
        #forward
        if dir == "F":

            #store actual pos
            pos_n = pos['N']
            pos_s = pos['S']            
            pos_e = pos['E']
            pos_w = pos['W']

            #compute forward advance
            dir_n = val * wpt['N']
            dir_s = val * wpt['S']
            dir_e = val * wpt['E']
            dir_w = val * wpt['W']

            # ugly but works
            # if opposite position is > to desired advance
            # substract from opposite direction
            # otherwise, substract opposite to desired advance, add result to desired direction
            # and set opposite to zero
            if dir_n > 0:
                if pos_s > dir_n:                    
                    pos['S'] -= dir_n if pos_s > 0 else 0
                else:
                    pos['S'] = 0
                    pos['N'] += dir_n - pos_s
            if dir_s > 0:
                if pos_n > dir_s:                    
                    pos['N'] -= dir_s if pos_n > 0 else 0
                else:
                    pos['N'] = 0
                    pos['S'] += dir_s - pos_n
            if dir_e > 0:
                if pos_w > dir_e:                    
                    pos['W'] -= dir_e if pos_w > 0 else 0
                else:
                    pos['W'] = 0
                    pos['E'] += dir_e - pos_w
            if dir_w > 0:
                if pos_e > dir_w:                    
                    pos['E'] -= dir_w if pos_e > 0 else 0
                else:
                    pos['E'] = 0
                    pos['W'] += dir_w - pos_e
            
        # rotate waypoint by checking compass
        elif dir == "L" or dir == "R":
            wpt = rotate_wpt(wpt, dir, val)
        # move waypoint (and respect opposite values)
        else:
            opposite = compass[dir][180]            
            if wpt[opposite] > 0 and wpt[opposite] >= val:
                wpt[opposite] -= val
            elif wpt[opposite] > 0 and wpt[opposite] < val:            
                wpt[dir] += val - wpt[opposite]
                wpt[opposite] = 0
            else:
                wpt[dir] += val    
                
    return functools.reduce(lambda a, b : a + b, list(map(lambda cord: pos[cord], pos)))

def rotate_wpt(wpt, dir, val):
    return {
        'N': wpt[compass['N'][(val if dir == "L" else (360-val))]],
        'S': wpt[compass['S'][(val if dir == "L" else (360-val))]],
        'E': wpt[compass['E'][(val if dir == "L" else (360-val))]],
        'W': wpt[compass['W'][(val if dir == "L" else (360-val))]],
    }    

print('result of part 1 is {}'.format(part1()))
print('result of part 2 is {}'.format(part2()))