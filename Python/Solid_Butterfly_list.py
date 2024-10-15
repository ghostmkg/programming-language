n = int(input())
for i in range (1,n+1):
    for j in range(i):
        print("*",end="")
    for k in range(1,((n-i)*2)):
        print(" ",end="")
    for l in range(i):
        if l==n-1:
            print(" ",end="")
        else:
            print("*",end="")
    print()
for i in range (n-1,0,-1):
    for j in range (i):
        print("*",end="")
    for k in range ((n-i)*2,1,-1):
        print(" ",end="")
    for l in range(i):
        print("*",end="")
    print()
