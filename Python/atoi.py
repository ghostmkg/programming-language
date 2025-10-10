def atoi(s: str) -> int:
    i = 0
    sign = 1
    result = 0
    n = len(s)
    
    # Skip leading spaces
    while i < n and s[i].isspace():
        i += 1
    
    # Check sign
    if i < n and (s[i] == '+' or s[i] == '-'):
        sign = -1 if s[i] == '-' else 1
        i += 1
    
    # Convert digits
    while i < n and s[i].isdigit():
        result = result * 10 + int(s[i])
        i += 1
    
    return sign * result

# Example usage:
print(atoi("   -789"))  # Output: -789
print(atoi("+42"))      # Output: 42
