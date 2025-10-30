def maxAbsoluteDegreeDiff(n, edgeList):
    in_degree = [0] * n
    out_degree = [0] * n

    for u, v in edgeList:
        out_degree[u] += 1
        in_degree[v] += 1

    max_diff = 0
    for i in range(n):
        diff = abs(in_degree[i] - out_degree[i])
        if diff > max_diff:
            max_diff = diff

    return max_diff
