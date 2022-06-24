from astarmaze import AStarMaze

rows_amount = 21
columns_amount = 21
maze = AStarMaze(rows_amount, columns_amount)
maze.print()
maze.solve_using_a_star_algorithm()
maze.print()
