import csv, sys

def get_input(file = 'input.csv'):
    with open(file, newline='') as csvfile:
        input = {"numbers": [], "grids": []}
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            if i == 0:
                input["numbers"] = row
                grid = Grid()
                continue
            if len(row) != 0:
                grid.add_row(row)
            if i%6 == 0:
                input["grids"].append(grid)
                grid = Grid()
    return input

def part1():
    input = get_input()
    for number in input["numbers"]:
        for grid in input["grids"]:
            grid.mark(number)
            if grid.wins():
                return grid.score()
    return None

def part2():
    input = get_input()
    c = 0
    for number in input["numbers"]:
        for grid in input["grids"]:
            if grid.won:
                continue
            grid.mark(number)
            if grid.wins():
                c += 1
                if c == len(input["grids"]):
                    return grid.score()
    return None


class Grid:     
    def __init__(self):
        self.cols, self.rows = [], []
        self.current = None
        self.won = False

    def add_row(self, row):
        self.rows.append([x for x in row[0].split(" ") if x != ""])

    def wins(self):
        self._reset_cols()
        for row in self.rows:
            if row.count("x") == len(row):
                self.won = True
                return True

        for col in self.cols:   
            if col.count("x") == len(col):
                self.won = True
                return True

        return False

    def mark(self, number):
        self.current = number
        for row in self.rows:
            for i, elt in enumerate(row):
                if elt == number:
                    row[i] = "x"

    def score(self):
        score = 0
        for row in self.rows:
            for elt in row:
                if elt != "x":
                    score += int(elt)
        return score * int(self.current)

    def _reset_cols(self):
        cols = [[] for x in range(len(self.rows[0]))]
        for row in self.rows:
            for i, val in enumerate(row):
                cols[i].append(val)
        self.cols = cols

print('result of part 1 is {}'.format(part1()))
print('result of part 2 is {}'.format(part2()))