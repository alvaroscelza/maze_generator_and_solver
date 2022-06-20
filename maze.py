import enum


class CellStatus(enum.Enum):
    Unknown = '0'
    Unexplored = '1'
    Visited = '2'
    Hampered = '3'


class Cell:
    _row_number: int
    _column_number = int
    status: CellStatus

    def __init__(self, row_number, column_number, status=CellStatus.Unknown):
        self._row_number = row_number
        self._column_number = column_number
        self.status = status

    def __repr__(self):
        return self.status.value


class Maze:
    grid = []

    def __init__(self, rows_amount, columns_amount):
        for row in range(rows_amount):
            self.grid.append([])
            for column in range(columns_amount):
                new_cell = Cell(row_number=row, column_number=column)
                self.grid[row].append(new_cell)
        self.generate_obstacles()

    def generate_obstacles(self):
        self.grid[3][3].status = CellStatus.Hampered
        self.grid[3][4].status = CellStatus.Hampered
        self.grid[3][5].status = CellStatus.Hampered
        self.grid[4][5].status = CellStatus.Hampered
        self.grid[5][5].status = CellStatus.Hampered
        self.grid[6][5].status = CellStatus.Hampered

    def print(self):
        print('')
        print('********************')
        for row in self.grid:
            print(row)
        print('********************')
        print('')

    # def solve_using_a_star_algorithm(self):
    #     start = grid[0][0]
