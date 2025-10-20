n = int(input())
for i in range(n):
    for j in range(i):
        print(" ",end=" ")
    for j in range(i,n-1):
        if i==0 or i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    for j in range(i,n):
        if i==0 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
for i in range(n-2,-1,-1):
    for j in range(i):
        print(" ",end=" ")
    for j in range(i,n-1):
        if i==0 or i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    for j in range(i,n):
        if i==0 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
