def calculate_distance(x1, y1, x2, y2):
    d=((x2-x1)**2+(y2-y1)**2)**0.5
    e=round(d,2)
    return e
x1,y1,x2,y2=map(int,input().split())
print(calculate_distance(x1,y1,x2,y2))
### ENTER THE INPUT IN A SINGLE LINE BY USING SPACES LIKE 1 2 4 7 ###