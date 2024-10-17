is_fahrenheit=int(input())
t=float(input())
if is_fahrenheit == 1:
    print(round((t-32)*5/9,4))
else:
    print(round((t*9/5) + 32,4))
