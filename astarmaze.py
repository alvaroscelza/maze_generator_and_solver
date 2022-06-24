import enum
import math

from colorama import Fore
from colorama import Style


class AStarCellStatus(enum.Enum):
    Unknown = '0'
    Discovered = '1'
    Visited = '2'
    Hampered = '3'
    SolutionPath = '4'


class AStarCell:
    _row_number: int
    _column_number = int

    status: AStarCellStatus
    came_from: 'AStarCell' or None
    cheapest_path_cost_from_start: float
    guess_of_how_cheap_from_start_to_goal_through_me: float

    @property
    def row_number(self):
        return self._row_number

    @property
    def column_number(self):
        return self._column_number

    def __init__(self, row_number, column_number, status=AStarCellStatus.Unknown):
        self._row_number = row_number
        self._column_number = column_number
        self.status = status
        self.came_from = None
        self.cheapest_path_cost_from_start = math.inf
        self.guess_of_how_cheap_from_start_to_goal_through_me = math.inf

    def __repr__(self):
        if self.status == AStarCellStatus.Unknown:
            return f"{Fore.BLACK}{self.status.value}{Style.RESET_ALL}"
        elif self.status == AStarCellStatus.Discovered:
            return f"{Fore.WHITE}{self.status.value}{Style.RESET_ALL}"
        elif self.status == AStarCellStatus.Visited:
            return f"{Fore.RED}{self.status.value}{Style.RESET_ALL}"
        elif self.status == AStarCellStatus.Hampered:
            return f"{Fore.BLUE}{self.status.value}{Style.RESET_ALL}"
        elif self.status == AStarCellStatus.SolutionPath:
            return f"{Fore.GREEN}{self.status.value}{Style.RESET_ALL}"
        else:
            # Failure: status non existent
            return 'something weird happened: this status is not recognized. {}'.format(self.status.value)


class AStarMaze:
    grid = []
    goal = None
    discovered_nodes = []

    def __init__(self, rows_amount, columns_amount):
        for row in range(rows_amount):
            self.grid.append([])
            for column in range(columns_amount):
                new_cell = AStarCell(row_number=row, column_number=column)
                self.grid[row].append(new_cell)
        self.goal = self.grid[3][18]
        self.goal.status = AStarCellStatus.SolutionPath
        self.generate_obstacles()

    def generate_obstacles(self):
        self.grid[6][5].status = AStarCellStatus.Hampered
        self.grid[6][6].status = AStarCellStatus.Hampered
        self.grid[6][7].status = AStarCellStatus.Hampered
        self.grid[6][8].status = AStarCellStatus.Hampered
        self.grid[6][9].status = AStarCellStatus.Hampered
        self.grid[6][10].status = AStarCellStatus.Hampered
        self.grid[6][11].status = AStarCellStatus.Hampered
        self.grid[6][12].status = AStarCellStatus.Hampered
        self.grid[6][13].status = AStarCellStatus.Hampered
        self.grid[6][14].status = AStarCellStatus.Hampered
        self.grid[6][15].status = AStarCellStatus.Hampered

        self.grid[7][5].status = AStarCellStatus.Hampered
        self.grid[7][6].status = AStarCellStatus.Hampered
        self.grid[7][7].status = AStarCellStatus.Hampered
        self.grid[7][8].status = AStarCellStatus.Hampered
        self.grid[7][9].status = AStarCellStatus.Hampered
        self.grid[7][10].status = AStarCellStatus.Hampered
        self.grid[7][11].status = AStarCellStatus.Hampered
        self.grid[7][12].status = AStarCellStatus.Hampered
        self.grid[7][13].status = AStarCellStatus.Hampered
        self.grid[7][14].status = AStarCellStatus.Hampered
        self.grid[7][15].status = AStarCellStatus.Hampered

        self.grid[8][5].status = AStarCellStatus.Hampered
        self.grid[8][6].status = AStarCellStatus.Hampered
        self.grid[8][7].status = AStarCellStatus.Hampered
        self.grid[8][8].status = AStarCellStatus.Hampered
        self.grid[8][9].status = AStarCellStatus.Hampered
        self.grid[8][10].status = AStarCellStatus.Hampered
        self.grid[8][11].status = AStarCellStatus.Hampered
        self.grid[8][12].status = AStarCellStatus.Hampered
        self.grid[8][13].status = AStarCellStatus.Hampered
        self.grid[8][14].status = AStarCellStatus.Hampered
        self.grid[8][15].status = AStarCellStatus.Hampered

        self.grid[9][13].status = AStarCellStatus.Hampered
        self.grid[9][14].status = AStarCellStatus.Hampered
        self.grid[9][15].status = AStarCellStatus.Hampered

        self.grid[10][13].status = AStarCellStatus.Hampered
        self.grid[10][14].status = AStarCellStatus.Hampered
        self.grid[10][15].status = AStarCellStatus.Hampered

        self.grid[11][13].status = AStarCellStatus.Hampered
        self.grid[11][14].status = AStarCellStatus.Hampered
        self.grid[11][15].status = AStarCellStatus.Hampered

        self.grid[12][13].status = AStarCellStatus.Hampered
        self.grid[12][14].status = AStarCellStatus.Hampered
        self.grid[12][15].status = AStarCellStatus.Hampered

        self.grid[13][13].status = AStarCellStatus.Hampered
        self.grid[13][14].status = AStarCellStatus.Hampered
        self.grid[13][15].status = AStarCellStatus.Hampered

    def print(self):
        print('')
        for row in self.grid:
            print(row)
        print('')

    def solve_using_a_star_algorithm(self):
        start = self.grid[-1][0]
        start.cheapest_path_cost_from_start = 0
        start.guess_of_how_cheap_from_start_to_goal_through_me = self.heuristic_function(start)
        self.discovered_nodes.append(start)

        while self.discovered_nodes:
            current_node = self.get_node_with_lowest_guest_of_how_cheap()
            current_node.status = AStarCellStatus.Visited
            self.print()
            if current_node == self.goal:
                # Success
                self.reconstruct_path()
                return True

            self.discovered_nodes.remove(current_node)
            current_neighbours = self.get_neighbours(current_node)
            for neighbour in current_neighbours:
                tentative_cheapest_path_from_start = current_node.cheapest_path_cost_from_start + self.distance(current_node, neighbour)
                if tentative_cheapest_path_from_start < neighbour.cheapest_path_cost_from_start or neighbour.cheapest_path_cost_from_start == math.inf:
                    neighbour.came_from = current_node
                    neighbour.cheapest_path_cost_from_start = tentative_cheapest_path_from_start
                    neighbour.guess_of_how_cheap_from_start_to_goal_through_me = tentative_cheapest_path_from_start + self.heuristic_function(neighbour)
                    if neighbour not in self.discovered_nodes:
                        neighbour.status = AStarCellStatus.Discovered
                        self.discovered_nodes.append(neighbour)
            self.print()
        return False  # Failure: discovered_nodes is empty but goal was not reached.

    def heuristic_function(self, cell):
        row_difference_to_goal = self.goal.row_number - cell.row_number
        column_difference_to_goal = self.goal.column_number - cell.column_number
        return max(row_difference_to_goal, column_difference_to_goal)

    def get_node_with_lowest_guest_of_how_cheap(self):
        current_lowest_guess = math.inf
        current_node_with_lowest_guess: AStarCell or None = None
        for node in self.discovered_nodes:
            if node.guess_of_how_cheap_from_start_to_goal_through_me < current_lowest_guess or node.guess_of_how_cheap_from_start_to_goal_through_me == math.inf:
                current_lowest_guess = node.guess_of_how_cheap_from_start_to_goal_through_me
                current_node_with_lowest_guess = node
        return current_node_with_lowest_guess

    def reconstruct_path(self):
        current_node = self.goal
        while current_node.came_from:
            current_node.status = AStarCellStatus.SolutionPath
            current_node = current_node.came_from
        current_node.status = AStarCellStatus.SolutionPath

    def get_neighbours(self, current_node):
        neighbours = []
        steps = [-1, 0, +1]
        for x in steps:
            for y in steps:
                if x == 0 and y == 0:
                    # This is the current_node, skip.
                    pass
                else:
                    current_row = current_node.row_number + x
                    current_column = current_node.column_number + y
                    negative_row_or_column = current_row < 0 or current_column < 0
                    surpassed_length = current_row >= len(self.grid) or current_column >= len(self.grid[current_row])
                    if negative_row_or_column or surpassed_length:
                        # We moved out of the grid, skip.
                        pass
                    else:
                        tentative_neighbour = self.grid[current_row][current_column]
                        if tentative_neighbour.status == AStarCellStatus.Hampered:
                            # We reached an obstacle, skip.
                            pass
                        else:
                            neighbours.append(self.grid[current_row][current_column])
        return neighbours

    @staticmethod
    def distance(current_node, neighbour):
        # Since this is a simple grid, every node is adjacent to its neighbours. Therefore, distance is 1.
        return 1
