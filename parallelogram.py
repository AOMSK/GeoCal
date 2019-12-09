"""parallelogram"""
import turtle
import tkinter as tk
from math import asin, degrees
root = tk.Tk()
screen = turtle.Screen()
root.title("Geometric Shape Calculator")
w_px = root.winfo_screenwidth()
h_px = root.winfo_screenheight()
#Estimation of the amount of pixel in a 1 cm line in any direction
px_cm = ((w_px / (root.winfo_screenmmwidth() / 10) + h_px / (root.winfo_screenmmheight() / 10)) / 2)

def parallelogram():
    """#Draw Parallelogram"""
    t = turtle.Turtle()
    side = turtle.textinput("Please input the size in cm", "base height vertical side")
    side = [float(i) for i in side.split()]
    side = [i * px_cm for i in side]
    sine = side[1] / side[2]
    lesser_angle = degrees(asin(sine))
    print(lesser_angle)
    for _ in range(2):
        t.forward(side[0])
        t.lt(180-(180-lesser_angle))
        t.forward(side[1]*1.5)
        t.lt(180-lesser_angle)
    return side
parallelogram()
