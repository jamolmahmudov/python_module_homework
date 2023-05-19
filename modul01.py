# Calculate the ceiling and floor values of a number
from math import floor,ceil

def calculate_ceiling_floor(number):
    """
    Calculates the ceiling and floor values of a number.

    Args:
        number (float): The number.

    Returns:
        tuple: A tuple containing the ceiling and floor values of the number.
    """
    a=(floor(number),ceil(number))
    return a
print(calculate_ceiling_floor(2.5))