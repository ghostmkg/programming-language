from collections import deque

def shortestPathBinaryMatrix(grid):
    n = len(grid)
    
    # If starting or ending cell is blocked
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return -1
    
    # Directions for 8 possible moves
    directions = [
        (1, 0), (-1, 0), (0, 1), (0, -1),
        (1, 1), (1, -1), (-1, 1), (-1, -1)
    ]
    
    # BFS queue -> (row, col, path_length)
    queue = deque([(0, 0, 1)])
    visited = set((0, 0))
    
    while queue:
        r, c, dist = queue.popleft()
        
        # If reached destination
        if r == n - 1 and c == n - 1:
            return dist
        
        # Explore all 8 directions
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            # Check if within bounds and cell is 0 (not blocked)
            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0 and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))
    
    # If no path found
    return -1
