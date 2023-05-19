# Round a decimal number to the nearest integer
from math import round 

def round_to_nearest_integer(number):
    """
    Rounds a decimal number to the nearest integer.

    Args:
        number (float): The decimal number.

    Returns:
        int: The nearest integer.
    """
    a=round(number)
    return a
print(round_to_nearest_integer(4.5))