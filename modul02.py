# Calculate the factorial of a number
from math import factorial

def calculate_factorial(number):
    """
    Calculates the factorial of a given number.

    Args:
        number (int): The number to calculate the factorial of.

    Returns:
        int: The factorial of the given number.
    """
    a=factorial(number)
    return a
print(calculate_factorial(5))