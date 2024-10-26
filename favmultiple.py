def find_largest_divisible(N):
    for num in range(N, 4, -1):
        if num % 5 == 0 or num % 7 == 0 or num % 11 == 0:
            return num
N = int(input())
print(find_largest_divisible(N))