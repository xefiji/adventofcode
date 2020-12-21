import csv, os, sys, time, re

def get_input(file = 'input.csv'):
    fileName = "{}/2020/day16/{}".format(os.getcwd(), file)
    input = {"rules" : {}, "your_ticket": [], "nearby_tickets": []}    
    key = "rules"
    with open(fileName, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        for row in reader:
            if len(row) == 0:
                continue
            if re.match(r"^your\sticket:$", row[0]):
                key = "your_ticket"
                continue
            elif re.match(r"^nearby\stickets:$", row[0]):
                key = "nearby_tickets"
                continue
            
            if key == "rules":
                r = row[0].split(": ")[1].split(" or ")
                rule_name = row[0].split(": ")[0]
                r1 = ">={}".format(r[0][:r[0].index("-")])
                r2 = "<={}".format(r[0][r[0].index("-")+1:])
                r3 = ">={}".format(r[1][:r[1].index("-")])
                r4 = "<={}".format(r[1][r[1].index("-")+1:])                
                input[key][rule_name] = [r1, r2, r3, r4]
            if key == "your_ticket":
                input[key] = row[0].split(",")        
            elif key == "nearby_tickets":
                input[key].append(row[0].split(","))  
                      
    return input

def part1():
    return sum(divide_valid_invalids(get_input())[1])

def is_invalid(val, rules):
    first_part_not_valid = eval("{}{}".format(str(val), rules[0])) is False \
        or eval("{}{}".format(str(val), rules[1])) is False
    second_part_not_valid = eval("{}{}".format(str(val), rules[2])) is False \
        or eval("{}{}".format(str(val), rules[3])) is False
    if first_part_not_valid is False or second_part_not_valid is False:
        return False
    return True

def divide_valid_invalids(input):
    valids, invalids = [], []
    for ticket in input["nearby_tickets"]:
        ticket_invalid = False
        for val in ticket:
            val_invalid = True
            for rule_name in input["rules"]:                             
                if is_invalid(val, input["rules"][rule_name]) is False:
                    val_invalid = False
            if val_invalid is True:
                ticket_invalid = True
                break              
        if ticket_invalid is False:
            valids.append(ticket)
        else: 
            invalids.append(int(val))
    return (valids, invalids)

def part2():
    input = get_input()            
    valids = divide_valid_invalids(input)[0]
    forbidden = {}

    # build all forbidden index
    for rule_name in input["rules"]:        
        forbidden[rule_name] = []
        for ticket in valids:            
            for i, val in enumerate(ticket):                
                if is_invalid(val, input["rules"][rule_name]):
                    forbidden[rule_name].append(i) 
    
    # sort them by most forbidden to most tolerant
    ordered = sorted(forbidden, key=lambda f: len(forbidden[f]), reverse=True)            

    # iterate over them by setting index to the one having the less possibilities
    res, passed = 1, []
    for rule in ordered:
        for i in range(len(input['your_ticket'])):
            if i not in forbidden[rule] and i not in passed:                
                if re.match(r"^departure", rule) is not None:
                    res *= int(input['your_ticket'][i]) # compute if departure
                passed.append(i)
                break
    
    return res
    
print('result of part 1 is {}'.format(part1()))
print('result of part 2 is {}'.format(part2()))