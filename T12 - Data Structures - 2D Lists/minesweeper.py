"""
hyperiondev - Software Engineering (Fundamentals)
Task 12 - "Data Structures - 2D Lists"
Author: Helder P - HP24010013265
Date: 16/04/2024

Description: Practical Task 1 - "minesweeper.py"
"""

def count_adjacent_mines(grid, row, col):
    # Define the relative positions of adjacent cells
    positions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]

    mine_count = 0
    rows = len(grid)
    cols = len(grid[0])

    # Iterate over relative positions
    for dr, dc in positions:
        # Calculate the adjacent cell's coordinates
        adj_row, adj_col = row + dr, col + dc

        # Check if the adjacent cell is within bounds
        if 0 <= adj_row < rows and 0 <= adj_col < cols:
            # If the adjacent cell contains a mine, increment mine_count
            if grid[adj_row][adj_col] == "#":
                mine_count += 1

    return str(mine_count)


def minesweeper(grid):
    rows = len(grid)
    cols = len(grid[0])

    # Create a new grid to store the result
    result = [["" for _ in range(cols)] for _ in range(rows)]

    # Iterate through each cell of the grid
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == "-":
                # If the cell is empty, count adjacent mines
                result[i][j] = count_adjacent_mines(grid, i, j)
            else:
                # If the cell contains a mine, keep it as is
                result[i][j] = "#"

    return result


if __name__ == "__main__":
    input_grid = [
        ["-", "-", "-", "#", "#"],
        ["-", "#", "-", "-", "-"],
        ["-", "-", "#", "-", "-"],
        ["-", "#", "#", "-", "-"],
        ["-", "-", "-", "-", "-"]
    ]

    output_grid = minesweeper(input_grid)

    # Print the output grid
    for row in output_grid:
        print(row)
