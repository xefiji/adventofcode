import sys, os

def wins(a, b, part):
    scale = 'ABC'
    winners = {f"{x}{scale[i+1] if i < len(scale)-1 else scale[0]}": 6 for i, x in enumerate(scale)}
    draws = {f"{x}{x}": 3 for x in scale}
    loosers = {f"{x[1]}{x[0]}": 0 for x in winners.keys()}
    scores = winners | draws | loosers

    weapon_score = lambda weapon: 1 if weapon in ['A','X'] else (2 if weapon in ['B','Y'] else 3) 

    if part == 1:            
        return scores[f"{a}{scale['XYZ'.index(b)]}"] + weapon_score(b)

    find = lambda score, scores: next(filter(lambda res: res is not None, [(x, scores[x]) if x[0] == a and scores[x] == score else None for x in scores]))    
    res = find( {'X': 0, 'Y': 3, 'Z': 6}[b], scores)
    return res[1] + weapon_score(res[0][1])

def part1():
    rounds = [tuple(x.split(' ')) for x in list(open('input.txt').read().splitlines())]
    return sum([wins(round[0], round[1], 1) for round in rounds])


def part2():    
    rounds = [tuple(x.split(' ')) for x in list(open('input.txt').read().splitlines())]
    return sum([wins(round[0], round[1], 2) for round in rounds])

print('result of part 1 is {}'.format(part1()))
print('result of part 2 is {}'.format(part2()))
