A, B=map(int,input().split())
sum=0
for i in range(A,B+1):
    fact=1
    for j in range(1,i+1):
        fact*=j
    sum+=fact
print(sum)