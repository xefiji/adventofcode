def resolve(turns):
    store = {i: 0 for i in range(9)}
    for num in list(map(int, open('input.csv').read().split(','))):
        store[num] += 1

    for j in range(turns):
        new_store = {i: 0 for i in range(9)}
        for num in reversed(store):
            if store[num] == 0:
                continue
            if num != 0:
                new_store[num -1] += store[num]
            if num == 0:
                new_store[6] += store[num]
                new_store[8] += store[num]
        store = new_store

    return sum(val for val in store.values())

print('result of part 1 is {}'.format(resolve(80)))     # part1
print('result of part 2 is {}'.format(resolve(256)))    # part2