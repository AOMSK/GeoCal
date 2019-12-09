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
    side = [float(i)*px_cm for i in side.split()]
    angle_A = degrees(acos((side[1]**2 + side[2]**2 - side[0]**2)/(2*side[1]*side[2])))
    angle_B = degrees(acos((side[2]**2 + side[0]**2 - side[1]**2)/(2*side[2]*side[0])))
    angle_C = degrees(acos((side[0]**2 + side[1]**2 - side[2]**2)/(2*side[0]*side[1])))
    t.fd(side[0])
    t.lt(180-angle_C)
    t.fd(side[1])
    t.lt(180-angle_A)
    t.fd(side[2])

    print("Angles A is %.2f"%angle_A)
    print("Angles B is %.2f"%angle_B)
    print("Angles C is %.2f"%angle_C)

triangle()
