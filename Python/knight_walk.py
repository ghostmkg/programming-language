from collections import deque

def knightWalk(rows, cols, start_row, start_col, dest_row, dest_col):
    moves = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]

    visited = [[False] * cols for _ in range(rows)]
    queue = deque([(start_row, start_col, 0)])
    visited[start_row][start_col] = True

    while queue:
        current_row, current_col, distance = queue.popleft()

        if current_row == dest_row and current_col == dest_col:
            return distance

        for dr, dc in moves:
            new_row = current_row + dr
            new_col = current_col + dc

            if 0 <= new_row < rows and 0 <= new_col < cols and not visited[new_row][new_col]:
                visited[new_row][new_col] = True
                queue.append((new_row, new_col, distance + 1))

    return -1