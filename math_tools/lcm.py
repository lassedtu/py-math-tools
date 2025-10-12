from .gcd import gcd

def lcm(a, b):
    """
    Calculates the least common multiple of two integers.
    Args:
        a: An integer.
        b: An integer.
    Returns:
        The least common multiple of a and b, None if the lcm is undefined.
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise Exception("The variables a and b must both be integers!")

    a = abs(a)
    b = abs(b)

    g = gcd(a, b)
    if g is None:
        return None
    lcm = (a * b) // g
    return lcm
