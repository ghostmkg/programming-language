def Surface_Area(l, b, h):
    return 2 * (l * b + b * h + h * l)

def Volume(l, b, h):
    return l * b * h

l, b, h = map(int, input().split())

print(Surface_Area(l, b, h), Volume(l, b, h))