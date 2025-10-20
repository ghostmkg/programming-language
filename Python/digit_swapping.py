def swap_digits(number):
    swapped = int(str(number)[::-1])
    return swapped

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print("Swapped digits:", swap_digits(num))