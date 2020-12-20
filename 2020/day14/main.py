import csv, os, sys, functools, re, itertools

def get_input(file = 'input.csv'):
    fileName = "{}/2020/day14/{}".format(os.getcwd(), file)
    input = []
    with open(fileName, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            input.append(row[0])            
    return input

def get_program():
    program, current = [], []
    input = get_input()
    for i, instr in enumerate(input):
        type, val = instr.split(' = ')
        if((type == "mask") and i > 0):            
            program.append(current)
            current = []            
        current.append({"type": type, "val": val})
    program.append(current)
    return program

def part1():    
    memory = {}
    for program in get_program():
        mask = program[0]["val"]
        for j in range(1, len(program)):
            memory[re.search(r"mem\[([0-9]+)\]", program[j]["type"]).group(1)] = int("".join(reversed([(lambda i, l, inversion, bin : bin[i] if l == "X" or l == bin[i] else inversion[bin[i]])(i, l, {"0": "1", "1": "0"}, (lambda bin: list("".join(["0" for c in range(len(bin), 36)]) + bin))("{:b}".format(int(program[j]["val"])))) for i, l in reversed(list(enumerate(mask)))])), 2)
    return sum(memory.values())

def part2():
    memory = {}            
    for program in get_program():
        mask = program[0]["val"]
        
        for j in range(1, len(program)):
            mem = int(re.search(r"mem\[([0-9]+)\]", program[j]["type"]).group(1))              
            bin = (lambda bin: list("".join(["0" for c in range(len(bin), len(mask))]) + bin))("{:b}".format(mem))                    
            for i, l in reversed(list(enumerate(mask))):                
                if l == "0":
                    continue
                bin[i] = {"X": "X", "1": "1"}[l]
                                            
            cpl, bin = bin[:bin.index('X')], bin[bin.index('X'):]            
            start = "".join("0" for elt in bin if elt == "X")
            end = "".join("1" for elt in bin if elt == "X")                                
            
            for i in range(int(start, 2), int(end, 2) + 1):                
                tobin = "{:b}".format(i)
                binlist = list("".join(["0" for char in range(len(tobin), len(start))]) + tobin)
                tmp = bin.copy()              
                occ = 0
                for k, char in enumerate(bin):                    
                    if char == "X":
                        tmp[k] = binlist[occ]
                        occ += 1                                 
                memory["".join(cpl + tmp)] = int(program[j]["val"])        

    return sum(memory.values())    

print('result of part 1 is {}'.format(part1()))
print('result of part 2 is {}'.format(part2()))