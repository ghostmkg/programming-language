def tri(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1

    trib = [0] * (n + 1)
    trib[0], trib[1], trib[2] = 0, 1, 1

    for i in range(3, n + 1):
        trib[i] = trib[i - 1] + trib[i - 2] + trib[i - 3]

    return trib[n]