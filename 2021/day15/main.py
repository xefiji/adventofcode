import heapq

def part1():
    lines = list(map(lambda x: list(map(lambda x:int(x), list(x))), open('input.csv').read().split('\n')))            
    graph = {"{},{}".format(y,x): get_neighboors(lines, x, y) for y, line in enumerate(lines) for x, _ in enumerate(line) }
    
    res = dijkstra(graph, '0,0')
    return res[list(graph)[-1]]

def part2():
    lines = list(map(lambda x: list(map(lambda x:int(x), list(x))), open('input.csv').read().split('\n')))            

    new_grid = []
    for _, line in enumerate(lines):
        new_line = current = line
        for _ in range(4):
            current = list(map(lambda x: x+1 if x < 9 else 1, current))
            new_line.extend(current)
        new_grid.append(new_line)

    block = lines
    for _ in range(4):
        for _, line in enumerate(block):
                current = list(map(lambda x: x+1 if x < 9 else 1, line))
                new_grid.append(current)
        block = new_grid[-len(lines):]

    graph = {"{},{}".format(y,x): get_neighboors(new_grid, x, y) for y, line in enumerate(new_grid) for x, _ in enumerate(line) }

    res = dijkstra(graph, '0,0')
    return res[list(graph)[-1]]

def get_neighboors(lines, x, y):
    up = int(lines[y-1][x]) if y > 0 else None
    right = int(lines[y][x+1]) if x < len(lines[y])-1 else None
    down = int(lines[y+1][x]) if y < len(lines)-1 else None
    left = int(lines[y][x-1]) if x > 0 else None

    n = {}
    if up is not None:
        n["{},{}".format(y-1,x)] = up
    if right is not None:
        n["{},{}".format(y,x+1)] = right
    if down is not None:
        n["{},{}".format(y+1,x)] = down
    if left is not None:
        n["{},{}".format(y,x-1)] = left

    return n

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    queue = [(0, start)]

    while len(queue) > 0:
        current_distance, current_vertex = heapq.heappop(queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            new_distance = current_distance + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(queue, (new_distance, neighbor))
                    
    return distances

print('result of part 1 is {}'.format(part1()))
print('result of part 2 is {}'.format(part2()))