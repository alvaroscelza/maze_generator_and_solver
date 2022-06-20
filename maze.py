class Maze:
    grid = []

    def __init__(self, rows_amount, columns_amount):
        for row in range(rows_amount):
            self.grid.append([])
            for column in range(columns_amount):
                self.grid[row].append(0)
        self.generate_obstacles()

    def generate_obstacles(self):
        self.grid[3][3] = 2
        self.grid[3][4] = 2
        self.grid[3][5] = 2
        self.grid[4][5] = 2
        self.grid[5][5] = 2
        self.grid[6][5] = 2

    def print(self):
        print('')
        print('********************')
        print('')
        for row in self.grid:
            print(row)
        print('********************')
        print('')
