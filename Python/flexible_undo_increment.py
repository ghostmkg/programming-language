def flexible_undo(n, q, operations):
    nums = [0] * n
    stack = []

    for op in operations:
        if op[0] == 1:
            i = op[1]
            nums[i] += 1
            stack.append(i)
        else:  
            k = op[1]
            undo_count = min(k, len(stack))
            for _ in range(undo_count):
                idx = stack.pop()
                nums[idx] -= 1

    return nums


n, q = map(int, input().split())
operations = []
for _ in range(q):
    ops = list(map(int, input().split()))
    operations.append(ops)

result = flexible_undo(n, q, operations)
print(*result)
