def gcd(a, b):
    """
    Calculates the greatest common divisor of two integers using the Euclidean algorithm.

    Args:
        a: An integer.
        b: An integer.

    Returns:
        The greatest common divisor of a and b.
    """
    if not isinstance(a, int) or not isinstance(b, int): # Throw an error if a and b are not integers
        raise Exception("The variables must be integers!")
    
    if a<0:
        a = a * -1 # Make sure a = |a|
    
    if b<0:
        b = b * -1 # Make sure b = |b|

    while a != b: # Loop until a and b are equal
        if b-a>0: # If a can be subtracted from b without b becoming negative
            b = b-a # Do it
        elif b-a<0: # If that's not the case a>b (since the loop would have stopped if a=b)
            a = a-b # Subtract b from a

    return a # Return a since a and b are the same (the greatest common divisor of a and b's original values)