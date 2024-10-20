def is_prime(n):       
    if n<=1:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    for i in range(3,int((n)**0.5)+1):
        if n%i==0:
            return False
    return True
n=int(input())
if is_prime(n):
    print("YES")
else:
    print("NO")