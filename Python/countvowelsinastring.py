s = "Python Programming"
vowels = "aeiouAEIOU"
count = 0

for char in s:
    if char in vowels:
        count += 1

print("Number of vowels:", count)
