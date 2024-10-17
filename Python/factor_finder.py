def find_factors(n): # TAKING INPUT
    for i in range(1,n+1):    #APPLYING LOOPS 
        if n%i==0:             #CONDITIONING FOR FACTORS
            print(i,end=" ")
a=int(input())
find_factors(a)