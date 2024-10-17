def calculate_distance(x1, y1, x2, y2):
    return round(((x2-x1)**2 + (y2-y1)**2)**.5,2)
x1,y1,x2,y2 = map(int, input().split())
print(calculate_distance(x1, y1, x2, y2))
