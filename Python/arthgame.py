def loop_calculator():
    """Calculator with loop - keep calculating"""
    print("Calculator (type 'quit' to exit)")
    print("-" * 30)
    
    while True:
        try:
            a = float(input("Number 1: "))
            op = input("Operation (+, -, *, /): ")
            b = float(input("Number 2: "))
            
            result = eval(f"{a}{op}{b}") if op in ['+', '-', '*', '/'] else None
            print(f"Result: {result}\n")
        except:
            print("Invalid input!\n")