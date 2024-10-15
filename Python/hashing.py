# hashing


def custom_hash(n):
    d = n[-1]
    rv = int(d)
    return rv


# Initialize the list
a = ["-1", "-2", "-3", "-4", "-5", "-6", "-7", "-8", "-9", "-10"]

# Store seat numbers
for k in range(5):
    s = input("Enter the seat number: ")
    i = custom_hash(s)
    a[i] = s

# Retrieve seat number
s = input("Enter the seat number to check: ")
i = custom_hash(s)

# Check if the seat number is in the list
if s not in a[i]:
    print("Value is not in the list")
else:
    print("Value is present in the list")
    b = []
    for j in range(len(a)):
        if len(a[j]) > 1:
            b.append(a[j])
    print(b)