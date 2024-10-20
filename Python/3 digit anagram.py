num1,num2=map(int,input().split())
def are_anagrams(num1, num2):
    a = num1%10
    num1//=10
    b = num1%10
    c = num1//10
    d = num2%10
    num2//=10
    e = num2%10
    f = num2//10
    if a == d:
        if b==e:
            if c==f:
                print(True)
            else:
                print(False)
        elif b==f:
            if c==e:
                print(True)
            else:
                print(False)
        else:
            print(False)
    elif a == e:
        if b==d:
            if c==f:
                print(True)
            else:
                print(False)
        elif b==f:
            if c==d:
                print(True)
            else:
                print(False)
        else:
            print(False)
    elif a == f:
        if b==d:
            if c==e:
                print(True)
            else:
                print(False)
        elif b==e:
            if c==d:
                print(True)
            else:
                print(False)
        else:
            print(False)
    else:
        print(False)

are_anagrams(num1, num2)
