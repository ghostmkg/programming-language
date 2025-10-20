def menu_calculator():
    """Calculator with menu options"""
    print("=" * 30)
    print("ARITHMETIC CALCULATOR")
    print("=" * 30)
    
    while True:
        print("\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")
        choice = input("Choose (1-5): ")
        
        if choice == '5':
            break
        
        try:
            a = float(input("Number 1: "))
            b = float(input("Number 2: "))
            
            if choice == '1':
                print(f"Result: {a + b}\n")
            elif choice == '2':
                print(f"Result: {a - b}\n")
            elif choice == '3':
                print(f"Result: {a * b}\n")
            elif choice == '4':
                print(f"Result: {a / b if b != 0 else 'Error!'}\n")
        except ValueError:
            print("Invalid input!\n")