import sys, math

def part1():
    raw = open('input.csv').read().split("\n")
    template = list(raw[0])
    rules = {x[0]: x[1] for x in map(lambda x: x.split(" -> "), raw[2:])}
    
    for _ in range(10):
        template = generate(template, [], rules)
    
    letter_max = template.count(max(template, key=template.count))
    letter_min = template.count(min(template, key=template.count))
  
    return letter_max - letter_min

def generate(template, generated, rules, start = 0):
    if start >= len(template)-1:
        return generated

    part = template[start:start+2]
    if len(generated) == 0:
        generated.append(part[0])
    
    generated.extend([rules[''.join(part)], part[1]])
    return generate(template, generated, rules, start+1)

def part2(): 
    return None

sys.setrecursionlimit(300000)
print('result of part 1 is {}'.format(part1()))
print('result of part 2 is {}'.format(part2()))