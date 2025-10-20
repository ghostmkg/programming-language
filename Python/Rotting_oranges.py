import collections

def orangesRotting(grid):
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    q = collections.deque()
    fresh_oranges_count = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                q.append((r, c))
            elif grid[r][c] == 1:
                fresh_oranges_count += 1

    if fresh_oranges_count == 0:
        return 0

    minutes_passed = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while q:
        level_size = len(q)
        
        for _ in range(level_size):
            r, c = q.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh_oranges_count -= 1
                    q.append((nr, nc))
        if q:
            minutes_passed += 1

    return minutes_passed if fresh_oranges_count == 0 else -1

# Example usage:
grid = [[2,1,1],[1,1,0],[0,1,1]]
print(orangesRotting(grid))  # Output: 4    

# The function orangesRotting takes a grid as input and returns the minimum number of minutes
# that must elapse until no cell has a fresh orange. If this is impossible, it returns -1.