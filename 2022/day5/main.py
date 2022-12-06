import re, sys

def get_cols_and_procs():
    input = [x for x in list(open('input.txt').read().split("\n\n"))]    
    tmps = [crate.replace('[', ' ').replace(']', ' ').replace('','.') for crate in input[0].split('\n') ]    
    
    indexes = [i for i in range(3, len(tmps[0]), 8)]    
    crates = [[line[x] if line[x] != ' ' else None for x in indexes] for line in tmps]    

    cols = []
    for line in reversed(crates[:-1]):
        for i, col in enumerate(line):
            if len(cols) <= i:
                cols.append([])
            if col is not None:
                cols[i].append(col)

    procs = [list(map(lambda x: int(x), list(filter(lambda x:x not in ['from', 'move', 'to'], x.split(' '))))) for x in input[1].split('\n')]
    return cols, procs

def part1():
    cols, procs = get_cols_and_procs()
    for proc in procs:
        for i in range(proc[0]):            
            cols = move(cols, proc[1], proc[2])                    
        
    return ''.join([x.pop() for x in cols])

def move(cols, from_col, to_col, count = None):
    from_col -= 1
    to_col -= 1
    if count is None:
        elt = cols[from_col].pop()
        cols[to_col].append(elt)
    else:
        elts = cols[from_col][-count:]    
        cols[from_col] = cols[from_col][:-count]
        cols[to_col].extend(elts)    
    return cols


def part2():    
    cols, procs = get_cols_and_procs()    
    for proc in procs:                
        cols = move(cols, proc[1], proc[2], proc[0])         
    
    return ''.join([x.pop() for x in cols])

print('result of part 1 is {}'.format(part1()))
print('result of part 2 is {}'.format(part2()))
