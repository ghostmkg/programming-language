n= (map(int,input().split()))
l=len(str(n))
max1=0
max2=0
for i in n:
    if i>max1:
        max2=max1
        max1=i
    else: 
        if i>max2 and i!=max1:
            max2=i
print(max1,max2)