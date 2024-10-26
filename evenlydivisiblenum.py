import math

def find_lcm(n):
    lcm = 1
    for i in range(2, n + 1):
        lcm = lcm * i // math.gcd(lcm, i)
    return lcm

N = int(input())
print(find_lcm(N))