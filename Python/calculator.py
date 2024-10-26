def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def calculator():
    print("Welcome to the Simple Calculator!")
    print("--------------------------------")
    print("You can perform the following operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("Type 'exit' anytime to quit the calculator.")
    print("--------------------------------")

    operations = {
        '1': add,
        '2': subtract,
        '3': multiply,
        '4': divide
    }

    operation_symbols = {
        '1': '+',
        '2': '-',
        '3': '*',
        '4': '/'
    }

    while True:
        choice = input("\nSelect an operation (1/2/3/4): ").strip().lower()

        if choice == 'exit':
            print("Thank you for using the calculator. Goodbye!")
            break
        
        if choice in operations:
            num1 = get_number("Enter the first number: ")
            num2 = get_number("Enter the second number: ")

            result = operations[choice](num1, num2)
            symbol = operation_symbols[choice]
            print(f"\nResult: {num1} {symbol} {num2} = {result}")
        else:
            print("Invalid option! Please select a valid operation (1, 2, 3, or 4).")

        next_calculation = input("\nWould you like to perform another calculation? (yes/no): ").strip().lower()
        if next_calculation != 'yes':
            print("Thank you for using the calculator. Goodbye!")
            break

if __name__ == "__main__":
    calculator()