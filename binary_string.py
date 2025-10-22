import math
n=int(input())
k=int(n/2)
if n%2!=0:
    print(0)
elif n<2:
    print(0)
else:
    print(math.factorial(n)//(math.factorial(k)*(math.factorial(n-k))))
