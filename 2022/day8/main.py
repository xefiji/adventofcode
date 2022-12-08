import re, sys
from functools import reduce


def part1():
    return process(1)

def part2():        
    return process(2)

def process(part):
    input = [list(map(int, list(x))) for x in open('input.txt').read().splitlines()]
    sum = 0
    scores = []
    for y, line in enumerate(input):
        for x, elt in enumerate(line):
            if y == 0 or x == 0 or x == len(line) - 1 or y == len(input) - 1:
                sum += 1
                continue                

            left = [input[y][k] for k in range(x if part == 1 else x -1 , -1, -1)]
            right = [input[y][k] for k in range(x if part == 1 else x +1 , len(line))]
            top = [input[k][x] for k in range(y if part == 1 else y -1 , -1, -1)]
            bottom = [input[k][x] for k in range(y if part == 1 else y +1 , len(input))]

            if part == 1:
                if decreases(left) or decreases(right) or decreases(top) or decreases(bottom):
                    sum += 1
                    continue

            if part == 2:
                tree_score = [score(elt, left), score(elt, right), score(elt, top), score(elt, bottom)]
                scores.append(reduce(lambda x, y: x*y, tree_score))     


    return sum if part == 1 else max(scores)


def decreases(list):
    current = list[0]
    for i in range(len(list)):
        if i == 0:
            continue
        if list[i] >= current:
            return False                    
    return True

def score(tree, list):
    score = 0
    for i in range(len(list)):
        if list[i] >= tree:
            score += 1
            break
        score += 1                
    return score
    
print('result of part 1 is {}'.format(part1()))
print('result of part 2 is {}'.format(part2()))
