def change_initial_grid_bomb_symbol(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "O":
                grid[i][j] = "3"


# change neighbors to '.'
def detonate(grid, i, j):  
    rows = len(grid)
    columns = len(grid[i])
    grid[i][j] = "."
    if j - 1 >= 0:
        grid[i][j - 1] = "."
    if j + 1 <= columns - 1:
        grid[i][j + 1] = "."
    if i + 1 <= rows - 1:
        grid[i + 1][j] = "."
    if i - 1 >= 0:
        grid[i - 1][j] = "."


def update_bombs(grid, plantBomb=True):
    rows = len(grid)
    to_explode = []
    # loop through grid raws and columns, update bomb timer, add new bombs
    for i in range(rows): 
        columns = len(grid[i])
        for j in range(columns):
            if grid[i][j] == "3":
                grid[i][j] = "2"
            elif grid[i][j] == "2":
                grid[i][j] = "1"
            elif grid[i][j] == "1":
                to_explode.append([i, j])
            elif plantBomb and grid[i][j] == ".":
                grid[i][j] = "3"
    # explode all expired bombs
    for bomb in to_explode:
        detonate(grid, bomb[0], bomb[1])
    return grid


def change_bomb_numbers_for_output(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != ".":
                grid[i][j] = "O"


def bomberMan(n, grid):
    if n < 2:
        return grid
    grid = [list(line) for line in grid]  # creating a two dimensional list from grid
    change_initial_grid_bomb_symbol(grid)  # changes 'O' into 3
    grid = update_bombs(grid, False) 
    for i in range(n, 1, -1):
        grid = update_bombs(grid)  # updates grid every second
    change_bomb_numbers_for_output(grid)  # changed numbers into 'O' again

    return ["".join(line) for line in grid]  # create string list of raws