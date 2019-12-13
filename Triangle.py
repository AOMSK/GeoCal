import turtle
import tkinter as tk
from math import acos, degrees
root = tk.Tk()
screen = turtle.Screen()
root.title("Geometric Shape Calculator")
w_px = root.winfo_screenwidth()
h_px = root.winfo_screenheight()
#Estimation of the amount of pixel in a 1 cm line in any direction
px_cm = ((w_px / (root.winfo_screenmmwidth() / 10) + h_px / (root.winfo_screenmmheight() / 10)) / 2)

"""Triangle"""
def triangle():
    """Find the angle of the triangle"""
    t = turtle.Turtle()
    side = turtle.textinput("Please input the 3 sides in cm.", "A B C")
    side = [float(i) for i in side.split()]
    sidepx = [i*px_cm for i in side]
    angle_A = degrees(acos((side[1]**2 + side[2]**2 - side[0]**2)/(2*side[1]*side[2])))
    angle_B = degrees(acos((side[2]**2 + side[0]**2 - side[1]**2)/(2*side[2]*side[0])))
    angle_C = degrees(acos((side[0]**2 + side[1]**2 - side[2]**2)/(2*side[0]*side[1])))
    t.fd(sidepx[0])
    t.lt(180-angle_C)
    t.fd(sidepx[1])
    t.lt(180-angle_A)
    t.fd(sidepx[2])
    text = info_tri(side, angle_A, angle_B, angle_C)
    print(text)

def info_tri(side, angle_A, angle_B, angle_C):
    """Info of the triangle"""
    text = "The triangle perimeter is %.2f cm.  (P = a + b + c)  \n"%(side[0] + side[1] + side[2])
    text += "The angle A is %.2f degrees.  (b**2 + c**2 - a**2)/(2*b*c)\n"%angle_A
    text += "The angle B is %.2f degrees.  (c**2 + a**2 - b**2)/(2*c*a)\n"%angle_B
    text += "The angle C is %.2f degrees.  (a**2 + b**2 - c**2)/(2*a*b)"%angle_C
    return text

triangle()
