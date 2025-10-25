def gcd(a, b):
    """
    Calculate the Greatest Common Divisor (GCD) of two integers using
    the Euclidean Algorithm.

    Parameters:
        a (int): First number
        b (int): Second number

    Returns:
        int: The GCD of `a` and `b`
    """

    # Continue loop until the second number becomes zero
    while b != 0:
        # Update values: move `b` to `a`, and remainder of a/b to `b`
        a, b = b, a % b

    # When b becomes 0, `a` will contain the GCD
    return a


# Example usage
print(gcd(48, 18))  # Output: 6
