from typing import List

def product_except_self(nums: List[int]) -> List[int]:
    # Variant B: O(1) extra space (excluding output)
    n = len(nums)
    if n == 0:
        return []
    out = [1] * n

    # fill out with left products
    left_prod = 1
    for i in range(n):
        out[i] = left_prod
        left_prod *= nums[i]

    # multiply by right products on the fly
    right_prod = 1
    for i in range(n - 1, -1, -1):
        out[i] *= right_prod
        right_prod *= nums[i]

    return out
