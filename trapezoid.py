import math
"""Trapezoid"""
def main():
    """Draw trapezoid"""
    #enter trapezoid parts
    base_a = float(input("Enter the base A length: "))
    base_b = float(input("Enter the base B length: "))
    leg_a = float(input("Enter the leg A length: "))
    leg_b = float(input("Enter the legB length: "))
    height = float(input("Enter the height: "))
    #find base angles
    angles_1 = math.degrees(math.asin(height/leg_a))
    angles_2 = math.degrees(math.acos(height/leg_b))
    print("Base angles A is %.2f"%angles_1)
    print("Base angles B is %.2f"%angles_2)
main()
