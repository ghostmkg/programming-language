a=int(input("Enter the number:"))
for i in range(a+1):
    prime=a+i
    count=0
    check=False 
    for j in range(1,prime+1):
         if(prime%j==0):
              count+=1
    if count==2:
         check=True
    if check:
       n=i
       break

for i in range(a+1):
    prime=a-i
    count=0
    check=False 
    for j in range(1,prime+1):
         if(prime%j==0):
              count+=1
    if count==2:
         check=True
    if check:
       p=i
       break

if n>p:
    print("Nearest prime is",a+p)
else:
    print("Nearest prime is",a+n)
    
