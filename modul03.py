# Perform trigonometric calculations
from math import sin,cos,tan,radians

def perform_trigonometric_calculations(angle):
    """
    Performs trigonometric calculations for a given angle in degrees.

    Args:
        angle (float): The angle in degrees.

    Returns:
        tuple: A tuple containing the sine, cosine, and tangent of the angle.
    """
    a=(sin(angle),cos(angle),tan(angle))
    return a
print(perform_trigonometric_calculations(radians(0)))