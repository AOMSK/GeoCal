import turtle, re
import tkinter as tk
from math import pi, sin, asin, radians, degrees, sqrt, acos
root = tk.Tk()
screen = turtle.Screen()
root.title("Geometric Shape Calculator")
w_px = root.winfo_screenwidth()
h_px = root.winfo_screenheight()
#Estimation of the amount of pixel in a 1 cm line in any direction
px_cm = ((w_px / (root.winfo_screenmmwidth() / 10) + h_px / (root.winfo_screenmmheight() / 10)) / 2)
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
    angles_1 = degrees(asin(height/leg_a))
    angles_2 = degrees(acos(height/leg_b))
    #Turtle
    t = turtle.Turtle()
    t.fd(max(base_a, base_b))
    t.lt(90+(90-angles_1))
    t.fd(leg_a)
    t.lt(angles_1)
    t.fd(min(base_a, base_b))
    t.lt(90-angles_2)
    t.fd(leg_b)
    #Info for trapezoid
    text = "The area of this trapezoid is %0.2f sqcm."%(1/2*(size[0]+size[1])*size[4])
    text += "The Perimeter of this trapezoid is %0.2f cm."%(size[0]+size[1]+size[2]+size[3])
    text += "All angles in this trapezoid is %0.2f, %0.2f, %0.2f, %0.2f."%(angles_1, 180-angles_1, angles_2+90, 180-(angles_2+90))
    print(text)

main()
