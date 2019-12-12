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
    """#Draw Parallelograms"""
    t = turtle.Turtle()
    side = turtle.textinput("Please input the size in cm", "base height vertical side")
    side = [float(i) for i in side.split()] 
    sidepx = [i * px_cm for i in side]
    sine = side[1] / side[2]
    lesser_angle = degrees(asin(sine))
    for _ in range(2):
        t.forward(sidepx[0])
        t.lt(180-(180-lesser_angle))
        t.forward(sidepx[1])
        t.lt(180-lesser_angle)
    text = info_parall(side)
    print(text)
    return side

def info_parall(side):
    """Info of the parallelogram"""
    text = "The area of this parallelogram is %.2f sqcm.  (base x Height)| \n"%(side[0] * side[1])
    text += "The circumference of this parallelogram is %.2f cm.  (Sum of all the sides)|"%((side[0] * 2) + (side[2] * 2))
    return text

parallelogram()
