import math

def is_prime(n):
    """
        Checks if a given number is prime.

        Args:
            n: An integer to check.

        Returns:
            True if n is prime, False otherwise.
    """
    
    if not isinstance(n, int):
        raise Exception("The variable n must be an integer!")
    
    if n <= 1:
        return False
    
    if n == 2:
        return True
    
    if n % 2 == 0:
        return False

    # Check for factors only up to the square root of n
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True