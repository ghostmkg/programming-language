def Prime_in_range(n):
    is_prime=[1]*(n+1)
    is_prime[0]=is_prime[1]=0
    prime_num=[]
    for i in range(2,n+1):
        if is_prime[i]==1:
            for j in range(2*i,n+1,i):
                is_prime[j]=0
            prime_num.append(i)
    answer=f"Prime numbers less than {n}: {prime_num}"
    return answer
n=int(input())
print(Prime_in_range(n)) 