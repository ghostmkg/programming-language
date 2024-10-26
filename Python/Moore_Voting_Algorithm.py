def moore_voting(arr):
    candidate = None
    count = 0

    for num in arr:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1

    return candidate
