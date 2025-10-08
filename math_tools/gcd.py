def gcd(a, b):
    """
    Calculates the greatest common divisor of two integers using the Euclidean algorithm.

    Args:
        a: An integer.
        b: An integer.

    Returns:
        The greatest common divisor of a and b, None if the gcd is undefined.
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise Exception("The variables must be integers!")
    
    # If both are zero, gcd is undefined
    if a == 0 and b == 0:
        return None
    
    # Work with positive values since gcd is always positive
    a = abs(a)
    b = abs(b)
    
    # Keep replacing the larger number with the remainder
    # This is way faster than subtracting repeatedly
    while b != 0:
        temp = b
        b = a % b  # Get the remainder when dividing a by b
        a = temp   # Move b into a for the next round
    
    return a  # When b hits zero, a contains the gcd