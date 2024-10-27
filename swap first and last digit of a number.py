num = int(input())
def swap_first_last(num):
    d = 0
    r = num
    l = r%10
    while r>0:
        d+=1
        fd = r%10
        r//=10
    num = num - l + fd
    num = num - (fd*(10**(d-1))) + (l*(10**(d-1)))
    return num
