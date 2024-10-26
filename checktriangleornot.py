def is_triangle(A, B, C):
    if A + B + C == 180 and A > 0 and B > 0 and C > 0:
        return "YES"
    else:
        return "NO"

A, B, C = map(int, input().split())

print(is_triangle(A, B, C))