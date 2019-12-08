from math import *
import math
"""Triangle"""
def main():
    """Find the angle of the triangle"""
    angles_a = float(input("Enter the angles for a: "))
    angles_b = float(input("enter the angles for b: "))
    angles_c = float(input("enter the angles for c: "))
    sind_A = degrees(acos((angles_b**2 + angles_c**2 - angles_a**2)/(2*angles_b*angles_c)))
    sind_B = degrees(acos((angles_c**2 + angles_a**2 - angles_b**2)/(2*angles_c*angles_a)))
    sind_C = degrees(acos((angles_a**2 + angles_b**2 - angles_c**2)/(2*angles_a*angles_b)))

    print("Angles A is %.2f"%sind_A)
    print("Angles B is %.2f"%sind_B)
    print("Angles C is %.2f"%sind_C)

main()
