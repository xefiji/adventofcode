import csv, os, sys, time

def get_input(file = 'input.csv'):
    fileName = "{}/2020/day15/{}".format(os.getcwd(), file)
    input = []
    with open(fileName, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            input.append(row)            
    return input[0]

def bruteforce(target):
    tic = time.perf_counter()            
    input = get_input()    
    turn, turns = 1, {}
    last, num = 0, 0
    
    while turn <= target:
        if (turn - 1) < len(input):
            num = int(input[turn-1])                       
        else:
            num = 0 if len(turns[last]) == 1 else (turns[num][1] - turns[num][0])                   
        try:
            turns[num] = [turns[num][-1], turn]            
        except KeyError:
            turns[num] = [turn]

        last = num
        turn += 1 
            
    toc = time.perf_counter()            
    print(f"Done in {toc - tic:0.4f} seconds")
    return num
    
print('result of part 1 is {}'.format(bruteforce(2020)))
print('result of part 2 is {}'.format(bruteforce(30000000)))

