MOD = 10**9 + 7

def count_subsets_with_sum(nums, target_sum):
    n = len(nums)
    if target_sum == 0:
        return 1

    memo = [[-1] * (target_sum + 1) for _ in range(n)]

    def helper(index, remaining_sum):
        if remaining_sum == 0:
            return 1
        if index == 0:
            return 1 if nums[0] == remaining_sum else 0

        if memo[index][remaining_sum] != -1:
            return memo[index][remaining_sum]

        count_excluding = helper(index - 1, remaining_sum)
        count_including = 0
        if nums[index] <= remaining_sum:
            count_including = helper(index - 1, remaining_sum - nums[index])

        memo[index][remaining_sum] = (count_excluding + count_including) % MOD
        return memo[index][remaining_sum]

    return helper(n - 1, target_sum)