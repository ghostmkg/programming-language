def reverse_name(n):
    words = n.split()
    reversed_name = ""
    for i in range(len(words) - 1, -1, -1):
        if reversed_name:
            reversed_name += " "
        reversed_name += words[i]
    return reversed_name
n=input()
print(reverse_name(n))