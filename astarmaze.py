import enum
import math


class AStarCellStatus(enum.Enum):
    Unknown = '0'
    Discovered = '1'
    Visited = '2'
    Hampered = '3'


class AStarCell:
    _row_number: int
    _column_number = int

    status: AStarCellStatus
    came_from: 'AStarCell' or None
    cheapest_path_cost_from_start: float
    guess_of_how_cheap_from_start_to_goal_through_me: float

    def __init__(self, row_number, column_number, status=AStarCellStatus.Unknown):
        self._row_number = row_number
        self._column_number = column_number
        self.status = status
        self.came_from = None
        self.cheapest_path_cost_from_start = math.inf
        self.guess_of_how_cheap_from_start_to_goal_through_me = math.inf

    def __repr__(self):
        return self.status.value


class AStarMaze:
    grid = []

    def __init__(self, rows_amount, columns_amount):
        for row in range(rows_amount):
            self.grid.append([])
            for column in range(columns_amount):
                new_cell = AStarCell(row_number=row, column_number=column)
                self.grid[row].append(new_cell)
        self.generate_obstacles()

    def generate_obstacles(self):
        self.grid[3][3].status = AStarCellStatus.Hampered
        self.grid[3][4].status = AStarCellStatus.Hampered
        self.grid[3][5].status = AStarCellStatus.Hampered
        self.grid[4][5].status = AStarCellStatus.Hampered
        self.grid[5][5].status = AStarCellStatus.Hampered
        self.grid[6][5].status = AStarCellStatus.Hampered

    def print(self):
        print('')
        print('********************')
        for row in self.grid:
            print(row)
        print('********************')
        print('')

    def solve_using_a_star_algorithm(self):
        start = self.grid[0][0]
        start.cheapest_path_cost_from_start = 0
        start.guess_of_how_cheap_from_start_to_goal_through_me = self.heuristic_function(start)
        goal = self.grid[-1][-1]
        discovered_nodes = [start]

        while discovered_nodes:
            current_node = self.get_node_with_lowest_guest_of_how_cheap(discovered_nodes)
            if current_node == goal:
                return self.reconstruct_path(current_node)

            discovered_nodes.remove(current_node)
            current_neighbours = self.get_neighbours(current_node)
            for neighbour in current_neighbours:
                tentative_cheapest_path_from_start = neighbour.cheapest_path_cost_from_start + self.distance(current_node, neighbour)
                if tentative_cheapest_path_from_start < neighbour.cheapest_path_cost_from_start:
                    neighbour.came_from = current_node
                    neighbour.cheapest_path_cost_from_start = tentative_cheapest_path_from_start
                    neighbour.guess_of_how_cheap_from_start_to_goal_through_me = tentative_cheapest_path_from_start + self.heuristic_function(neighbour)
                    if neighbour not in discovered_nodes:
                        discovered_nodes.append(neighbour)
        return False  # Failure: discovered_nodes is empty but goal was not reached.

    def heuristic_function(self, cell):
        return 0

    def get_node_with_lowest_guest_of_how_cheap(self, discovered_nodes):
        return 0

    def reconstruct_path(self, current_node):
        pass

    def get_neighbours(self, current_node):
        return 0

    def distance(self, current_node, neighbour):
        return 0
