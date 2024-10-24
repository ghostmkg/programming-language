"""
This is a pyton implementation for validating parentheses for a given expression
"""

class ValidParentheses:
    def is_valid(expression: str) -> bool:
        stack = []
        brackets = {")":"(", "}":"{", "]":"["}

        for char in expression:
            if char in brackets.values():
                stack.append(char)
            elif char in brackets.keys():
                if not stack or brackets[char] != stack.pop():
                  return False
        
        return not stack

if __name__ == "__main__":
    import doctest

    doctest.testmod()

    exp = str(input("Enter the expression to evaluate"))

    print("The given expression")
    print(ValidParentheses.is_valid(exp))
