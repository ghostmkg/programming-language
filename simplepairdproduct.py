N = int(input())
A = list(map(int, input().split()))
result = [A[i] * A[i + 1] for i in range(0, N, 2)]
for num in result:
    print(num, end=' ')