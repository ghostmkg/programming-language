dir = "DLRU"
dr = [1, 0, 0, -1]
dc = [0, -1, 1, 0]

def isValid(r, c, n, maze):
    return 0 <= r < n and 0 <= c < n and maze[r][c] == 1

def findPath(r, c, maze, path, res):
    n = len(maze)
    if r == n - 1 and c == n - 1:
        res.append("".join(path))
        return

    maze[r][c] = 0  

    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if isValid(nr, nc, n, maze):
            path.append(dir[i])
            findPath(nr, nc, maze, path, res)
            path.pop()  

    maze[r][c] = 1  

def ratInMaze(maze):
    n = len(maze)
    result = []
    path = []

    if maze[0][0] == 1 and maze[n - 1][n - 1] == 1:
        findPath(0, 0, maze, path, result)

    result.sort()
    return result

if __name__ == "__main__":
    maze = [
        [1, 0, 0, 0],
        [1, 1, 0, 1],
        [1, 1, 0, 0],
        [0, 1, 1, 1]
    ]

    result = ratInMaze(maze)
    for p in result:
        print(p, end=" ")