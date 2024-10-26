def checkPerfectNumber(num):
    x=0
    for i in range(1,num):
        if num%i==0:
            x+=i
        else:
            pass
    if x==num:
        return True 
    else:
        return False
num=int(input())
print(checkPerfectNumber(num))
