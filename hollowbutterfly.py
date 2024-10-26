n=int(input())
for i in range(1,n+1):
    for j in range(1,2*n+1):
        if j==1 or j==2*n or i==j or j==2*n-i+1:
            print('*',end=' ')
        else:
            print(" ",end=' ')
    print()
for i in range(1,n):
    for j in range(1,2*n+1):
        if j==1 or j==2*n or j==n-i or j==n+i+1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()