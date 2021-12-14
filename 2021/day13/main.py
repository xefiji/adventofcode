def resolve(part=1):
    tmp = list(map(lambda x: x, open('input.csv').read().split("\n")))
    instructions = list(map(lambda x: [x[0], int(x[1])], map(lambda x: list(map(lambda x:x, x.replace('fold along ', '').split('='))), filter(lambda x: x.count('fold along') > 0, tmp))))
    coords = list(map(lambda x: list(map(int, x.split(','))), filter(lambda x: x.count(','), tmp)))
    
    coords_dict = {i[1]: [] for i in coords}
    for coord in coords:
        coords_dict[coord[1]].append(coord[0])

    for instruction in instructions:
        new_coords = []
        for coord in coords:
            
            new_x = coord[0]
            if (instruction[0] == "x" and coord[0] > instruction[1]):
                    new_x = instruction[1] - (coord[0] - instruction[1])

            new_y = coord[1]
            if instruction[0] == "y" and coord[1] > instruction[1]:
                new_y = instruction[1] - (coord[1] - instruction[1])

            new_coord = [new_x, new_y]
            new_coords.append(new_coord)

        coords_dict = {i[1]: [] for i in new_coords}
        for coord in new_coords:
            coords_dict[coord[1]].append(coord[0])
        
        max_x = max(list(map(lambda x:x[0], new_coords)))
        max_y = max(list(map(lambda x:x[1], new_coords))) 

        grid = []
        for y in range(max_y+1):
            row = []
            for x in range(max_x+1):
                try:
                    val = "#" if coords_dict[y].count(x) > 0 else "."
                except KeyError:
                    val = "."
                row.append(val)
            grid.append(row)

        total = 0
        for row in grid:
            total += row.count("#")
            if part == 2:
                print(" ".join(row))
        if part == 1:
            return total
        coords = new_coords
        print()
        
    return total

def part2():
    resolve(2)
    return "Read part 1's output"

print('result of part 1 is {}'.format(resolve(1)))
print('result of part 2 is {}'.format(part2()))