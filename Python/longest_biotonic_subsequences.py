def lbs(nums):
    n = len(nums)
    if n < 3:
        return 0  # A bitonic sequence needs at least 3 elements

    # Step 1: LIS from left to right
    lis = [1] * n
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    # Step 2: LDS from right to left
    lds = [1] * n
    for i in range(n - 2, -1, -1):
        for j in range(n - 1, i, -1):
            if nums[i] > nums[j] and lds[i] < lds[j] + 1:
                lds[i] = lds[j] + 1

    # Step 3: Combine LIS + LDS - 1
    max_len = 0
    for i in range(n):
        if lis[i] > 1 and lds[i] > 1:  # must increase and decrease
            max_len = max(max_len, lis[i] + lds[i] - 1)

    return max_len