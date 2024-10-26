n=int(input())
for i in range(n):
    k=i+1
    for j in range(i):
        print(' ',end='')
    for j in range(n-i):
        print(k,end=' ')
        k=k+1
    print()
for i in range(n-1,0,-1):
    p=i
    for j in range(i-1):
        print(' ',end='')
    for j in range(n-i+1):
        print(p,end=' ')
        p+=1
    print()