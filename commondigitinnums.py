def numbers(a,b):
    str_a = str(a)
    str_b = str(b)
    min_length = min(len(str_a), len(str_b))
    
    result = ""
    for i in range(min_length):
        if str_a[i] == str_b[i]:
            if result:
                result += " "
            result += str_a[i]
    
    return result
a,b=map(int, input().split())
print(numbers(a,b))