n = int(input())
for i in range(1,n+1):
    if i>1:
        print("*",end="")
        for j in range(1,2*i-2):
            print(" ",end="")
        print("*",end=" ")
        for k in range (2*(n -i)):
            print(" ",end=" ")
        print("*",end=" ")
        for j in range(1,2*i-3):
            print(" ",end="")
        print("*")
    else:
        print("*",end=" ")
        for j in range(1,2*(n-i)+1):
            print(" ",end=" ")
        print("*")
for i in range(n-1,0,-1):
    if i>1:
        print("*",end="")
        for j in range(1,2*i-2):
            print(" ",end="")
        print("*",end=" ")
        for k in range (2*(n -i)):
            print(" ",end=" ")
        print("*",end=" ")
        for j in range(1,2*i-3):
            print(" ",end="")
        print("*")
    else:
        print("*",end=" ")
        for j in range(1,2*(n-i)+1):
            print(" ",end=" ")
        print("*")
