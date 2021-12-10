import math

lines = list(map(list, open('input.csv').read().split("\n")))
opens = lambda x: x in ['<', '(', '[', '{']
matches = dict(zip('({[<)}]>',')}]>({[<'))
assoc = lambda x: matches[x]

# use lifo stack and break on corrupted lines
def part1():
    scores = lambda x: {'>': 25137, ')': 3, ']': 57, '}': 1197}[x]

    total = 0
    for line in lines:
        stack = []
        for char in line:
            if opens(char):
                stack.insert(0, char)
            elif assoc(char) != stack.pop(0):
                total += scores(char)
                break
    return total

# use lifo stack and continue if incomplete. Remaining stack is the completion pattern
def part2():
    scores = lambda x: {'>': 4, ')': 1, ']': 2, '}': 3}[x]
    
    totals = []
    for line in lines:
        stack, corrupted = [], False
        for char in line: 
            if opens(char):
                stack.insert(0, char)
            elif assoc(char) != stack.pop(0):
                corrupted = True
                break

        if corrupted:
            continue

        total = 0
        for char in list(map(assoc, stack)):
            total = (total * 5) + scores(char)
        totals.append(total)

    return sorted(totals)[math.floor(len(totals)/2)]

print('result of part 1 is {}'.format(part1()))
print('result of part 2 is {}'.format(part2()))