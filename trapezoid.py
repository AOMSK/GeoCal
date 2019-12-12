import turtle
from math import asin, acos, degrees
"""Trapezoid"""
def main():
    """Draw trapezoid"""
    #enter trapezoid parts
    size = turtle.textinput("Enter the sizes:", "Base_A Base_B Leg_A Leg_B Height")
    size = [float(i) for i in size.split()]
    base_a = size[0] * px_cm
    base_b = size[1] * px_cm
    leg_a = size[2] * px_cm
    leg_b = size[3] * px_cm
    height = size[4] * px_cm
    #find base angles
    angles_1 = math.degrees(math.asin(height/leg_a))
    angles_2 = math.degrees(math.acos(height/leg_b))
    print("Base angles A is %.2f"%angles_1)
    print("Base angles B is %.2f"%angles_2)

    t = turtle.Turtle()
    t.fd(max(base_a, base_b))
    t.lt(90+(90-angles_1))
    t.fd(leg_a)
    t.lt(angles_1)
    t.fd(min(base_a, base_b))
    t.lt(90-angles_2)
    t.fd(leg_b)

def info_trap(size, angles_1, angles_2):
    """Info of the trapezoid"""
    text = "The area of this trapezoid is %.2f sqcm. (1/2 x (Base_A+Base_B) x Height)|"%(1/2*(size[0]+size[1])*size[4])
    text += "The Perimeter of this trapezoid is %.2f cm. (Base_A+Base_B+Leg_A+Leg_B)"%(size[0]+size[1]+size[2]+size[3])
    text += "All angles in this trapezoid is %0.2f, %0.2f, %0.2f, %0.2f."%(angles_1, 180-angles_1, angles_2+90, 180-(angles_2+90))

main()
