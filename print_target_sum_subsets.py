def find_subsets(arr, target):
    result = []

    def backtrack(start, path, curr_sum):
        if curr_sum == target:
            result.append(path[:])
        if curr_sum >= target:
            return
        for i in range(start, len(arr)):
            path.append(arr[i])
            backtrack(i + 1, path, curr_sum + arr[i])
            path.pop()

    backtrack(0, [], 0)
    return result
