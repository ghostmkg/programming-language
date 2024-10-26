a,b,c = map(int, input().split())

youngest = oldest = 1

if a < b:
    if a < c:
        youngest = 1
    else:
        youngest = 3
else:
    if b < c:
        youngest = 2
    else:
        youngest = 3

if a > b:
    if a > c:
        oldest = 1
    else:
        oldest = 3
else:
    if b > c:
        oldest = 2
    else:
        oldest = 3

print(youngest, oldest)