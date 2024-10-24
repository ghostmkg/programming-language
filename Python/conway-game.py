import random
import os
import time


def create_grid(cols, rows):
    grid = [[random.randint(0, 1) for _ in range(cols)] for _ in range(rows)]
    # for _ in cols:
    #     for _ in rows:
    #         grid.append(random.randint(0, 1))
    #     grid.append()
    return grid


def display_grid(grid):
    for row in grid:
        for col in row:
            print(f"{col} ", end="")
        print()


def get_neighbor(grid):
    rows = len(grid)
    cols = len(grid[0])
    neighbors = [[0] * cols for _ in range(rows)]
    directions = [
        (-1, 1),
        (0, 1),
        (0, -1),
        (1, 1),
        (1, 0),
        (1, -1),
        (-1, 0),
        (-1, -1),
    ]
    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    neighbors[r][c] += 1

    return neighbors


# Any live cell with fewer than two live neighbors dies, as if by underpopulation.
# Any live cell with more than three live neighbors dies, as if by overpopulation.
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
# Any live cell with two or three live neighbors lives on to the next generation.


def update_grid(grid, neighbors):
    rows = len(grid)
    cols = len(grid[0])
    for r in range(rows):
        for c in range(cols):
            neighbor_num = neighbors[r][c]
            if neighbor_num < 2:
                grid[r][c] = 0
            elif neighbor_num > 3:
                grid[r][c] = 0
            elif neighbor_num == 3:
                grid[r][c] = 1

    return grid


if __name__ == "__main__":
    grid = create_grid(10, 10)
    while 1:
        os.system("clear")
        display_grid(grid)
        neighbors = get_neighbor(grid)
        update_grid(grid, neighbors)
        time.sleep(0.5)
