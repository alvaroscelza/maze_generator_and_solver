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
        return self.status.value


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
        self.goal = self.grid[-1][-1]
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
        self.discovered_nodes.append(start)

        while self.discovered_nodes:
            current_node = self.get_node_with_lowest_guest_of_how_cheap()
            if current_node == self.goal:
                return self.reconstruct_path()

            self.discovered_nodes.remove(current_node)
            current_neighbours = self.get_neighbours(current_node)
            for neighbour in current_neighbours:
                tentative_cheapest_path_from_start = neighbour.cheapest_path_cost_from_start + self.distance(current_node, neighbour)
                if tentative_cheapest_path_from_start < neighbour.cheapest_path_cost_from_start:
                    neighbour.came_from = current_node
                    neighbour.cheapest_path_cost_from_start = tentative_cheapest_path_from_start
                    neighbour.guess_of_how_cheap_from_start_to_goal_through_me = tentative_cheapest_path_from_start + self.heuristic_function(neighbour)
                    if neighbour not in self.discovered_nodes:
                        self.discovered_nodes.append(neighbour)
        return False  # Failure: discovered_nodes is empty but goal was not reached.

    def heuristic_function(self, cell):
        row_difference_to_goal = self.goal.row_number - cell.row_number
        column_difference_to_goal = self.goal.column_number - cell.column_number
        return max(row_difference_to_goal, column_difference_to_goal)

    def get_node_with_lowest_guest_of_how_cheap(self):
        current_lowest_guess = math.inf
        current__node_with_lowest_guess = math.inf
        for node in self.discovered_nodes:
            if node.guess_of_how_cheap_from_start_to_goal_through_me < current_lowest_guess:
                current_lowest_guess = node.guess_of_how_cheap_from_start_to_goal_through_me
                current__node_with_lowest_guess = node
        return current__node_with_lowest_guess

    def reconstruct_path(self):
        current_node = self.goal
        total_path = []
        while current_node.came_from:
            first_position = 0
            total_path.insert(first_position, current_node)
            current_node = current_node.came_from

    def get_neighbours(self, current_node):
        return 0

    def distance(self, current_node, neighbour):
        return 0
