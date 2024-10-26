username = input("Enter the username:")
length = len(username)
spaces = username.find("  ")
digits = username.isdigit()
if length >12:
    print("Your username can't have more than 12 letters")
elif not spaces == -1:
    print("Your username can't have spaces")
elif not digits == 0:
    print("Your username can't have digits")
else:
    print(f"Welcome {username}")


