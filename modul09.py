# Convert an angle from radians to degrees
from math import radians,degrees 

def convert_radians_to_degrees(radians):
    """
    Converts an angle from radians to degrees.

    Args:
        radians (float): The angle in radians.

    Returns:
        float: The angle in degrees.
    """
    a=degrees(radians)
    return a
print(convert_radians_to_degrees(0.7853981633974483))