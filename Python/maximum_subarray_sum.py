n = int(input())
arr = list(map(int, input().split()))

total = 0
max_sum = float('-inf')

for num in arr:
    total += num
    max_sum = max(max_sum, total)

    if total < 0:
        total = 0

print(max_sum)