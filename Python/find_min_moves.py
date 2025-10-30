def findMinMoves(machines):
    n = len(machines)
    total = sum(machines)
    if total % n != 0:
        return -1
    avg = total // n

    res = 0
    left_sum = 0  # sum of machines[0..i]
    for i, x in enumerate(machines):
        left_sum += x
        # need = how many dresses net should be moved from left side to right side
        need = left_sum - avg * (i + 1)
        # at position i we need at least these many moves:
        res = max(res, abs(need), x - avg)
    return res
