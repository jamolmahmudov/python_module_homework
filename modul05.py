# Calculate the exponential value of a number
from math import exp

def calculate_exponential(number):
    """
    Calculates the exponential value of a given number.

    Args:
        number (float): The number.

    Returns:
        float: The exponential value of the number.
    """
    a=exp(number)
    return a
print(calculate_exponential(1))