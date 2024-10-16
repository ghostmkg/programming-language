n = int(input())
for i in range(n,0,-1):
    for j in range(n-i):
        print( " ",end= " ")
    for j in range(2*i-1):
        if j == 0 or i == n or j == (2*i)-2:
            print("*",end = " ")
        else:
            print(" ",end = " ")
    print()
for i in range(2,n+1):
    for j in range(n-i):
        print( " ",end= " ")
    for j in range(2*i-1):
        if j == 0 or i == n or j == 2*i-2:
            print("*",end = " ")
        else:
            print(" ",end = " ")
    print()
