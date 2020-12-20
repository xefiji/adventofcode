import csv, os, sys, functools, time
from util import display_tstp, display

def get_input(file = 'input.csv'):
    fileName = "{}/2020/day13/{}".format(os.getcwd(), file)
    input = []
    with open(fileName, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        for row in reader:
            input.append(row[0])            
    return input

def part1():
    input = get_input() 
    departure, buses = int(input[0]), [id for id in input[1].split(",") if id != "x"]    
    start_waiting = departure
    while True:
        for bus in buses:        
            if departure % int(bus) == 0:
                return(departure - start_waiting) * int(bus)                
        departure += 1
            
# 200 sec for last example...way to long for real puzzle :/
def part2_bruteforce():
    tic = time.perf_counter()    
    buses = [id for id in get_input()[1].split(",")]    
    departure = -1
    while True:
        departure += 1        
        if departure % int(buses[0]) != 0:
            continue
        if (departure + (len(buses) -1)) % int(buses[len(buses)-1]) != 0:
            continue
                
        found = True
        for i in range(1, len(buses) - 1):            
            if buses[i] == "x":
                continue            
            if (departure + i) % int(buses[i]) != 0:
                found = False
                break        
                
        if found is True:
            toc = time.perf_counter()            
            print(f"Done in {toc - tic:0.4f} seconds")
            return departure    


print('result of part 1 is {}'.format(part1()))
print('result of part 2 is {}'.format(part2_bruteforce()))
