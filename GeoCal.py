"""
Geometric Shape Calculator
A calculator and graphic representator for geometric shapes.

Created By
62070025 Janisda Mukda
62070088 Tawatchai Hanon
62070115 Parkorn Kampao
62070124 Piyaporn Phutpore
62070196 Sipang Klinhom
"""

import turtle
import tkinter as tk
from math import pi, sin, asin, radians, degrees, sqrt
root = tk.Tk()
screen = turtle.screen()
root.title("Geometric Shape Calculator")
w_px = root.winfo_screenwidth()
h_px = root.winfo_screenheight()
#Estimation of the amount of pixel in a 1 cm line in any direction
px_cm = ((w_px / (root.winfo_screenmmwidth() / 10) + h_px / (root.winfo_screenmmheight() / 10)) / 2)

def main():
    """Main part of the programme.
    Works by taking an input, call the drawing functions,
    calculate the informations,
    then output the informations through tkinter."""
    screen.title("Graphic Representation")
    screen.screensize(w_px//2, h_px//2)
    shape = turtle.textinput("Geometric Shape Calculator", "Please input your desired shaped:")
    shape = shape.lower()
    bob = turtle.Turtle()
    bob.delay = 1e-20 #set the turtle drawing speed
    shapelist = {"square": square, "circle": circle, "rectangle": recta, "ellipse": ellipse}
    info = shapelist[shape](bob)
    bob.hideturtle()
    shape_info(shape, info)

#Quadrilaterals
def square(t):
    """Draw a square"""
    lenght = turtle.textinput("Please input the size", "in cm")
    lenght = 10 if lenght == "" else float(lenght)
    lenghtpx = lenght * px_cm
    lenghtpx = w_px/3 if lenghtpx > w_px//2 else lenghtpx
    polygon(t, 4, lenghtpx)
    return lenght

def recta(t):
    """Draw a quadrilateral"""
    side = turtle.textinput("Please input the size in cm", "side1 side2")
    side = [float(i) for i in side.split()]
    side = [5, 10] if side == [] else side
    sidepx = [i*px_cm for i in side]
    ratio = sidepx[0] / sidepx[1] #will be used if input is too large to draw
    sidepx = [(w_px/3)*ratio, w_px/3] if any([sidepx[0] > w_px//2, sidepx[1] > w_px//2]) else sidepx
    for _ in range(2):
        t.fd(sidepx[0])
        t.lt(90)
        t.fd(sidepx[1])
        t.lt(90)
    return side

#Ovals
def circle(t):
    """Draw a circle of a certain radius"""
    radius = turtle.textinput("Please input the radius", "in cm")
    radius = 5 if radius == "" else float(radius)
    radiuspx = radius * px_cm
    radiuspx = w_px/3 if radiuspx > w_px//2 else radiuspx
    arc(t, radiuspx)
    return radius

def ellipse(t):
    """Draw an ellipse"""
    radius = turtle.textinput("Please enter the radiuses", "Minor Major\nin cm")
    radius = [50, 100] if radius == "" else [float(i) for i in radius.split()]
    radiuspx = [i*px_cm for i in radius]
    ratio = radiuspx[0] / radiuspx[1] #will be used if input is too large to draw
    radiuspx = [(w_px/3)*ratio, w_px/3] if any([radiuspx[0] > w_px//2, radiuspx[1] > w_px//2]) else radiuspx
    t.rt(45)
    arc(t, radiuspx[1], 90)
    arc(t, radiuspx[0], 90)
    arc(t, radiuspx[1], 90)
    arc(t, radiuspx[0], 90)
    return radius

#Draw the lines
def arc(t, radius=50, angle=360.0):
    """Draw an arc"""
    side = int(angle//(radius//10)) + 10
    lenght = (pi * radius * 2.0)/side
    angle /= side
    polyline(t, side, lenght, angle)

def polyline(t, side, lenght, angle):
    """Draw many lines"""
    for _ in range(side):
        t.fd(lenght)
        t.lt(angle)

def polygon(t, side=6, lenght=100):
    """Draw a polygon of a certain side lenght and edges"""
    angle = 360.0/side
    polyline(t, side, lenght, angle)

#Shows the infomations
def shape_info(name, shape_data):
    """Output the calculations"""
    info_dict = {"square": info_sq, "rectangle": info_rect, "circle": info_circ, "ellipse": info_ell}
    T = tk.Text(root)
    T.pack()
    T.insert(tk.END, info_dict[name](shape_data))

def info_sq(side):
    """Info of the square"""
    text = "The area of this square is %.3f sqcm.\n(Side^2)\n"%(side**2)
    text += "The circumference of this square is %.3f cm\n(Side x 4)\n"%(side*4)
    text += "All four corners of a square are right angles (90°)."
    return text

def info_rect(side):
    """Info of the rectangle"""
    text = "The area of this rectangle is %.3f sqcm.\n(Width x Height)\n"%(side[0] * side[1])
    text += "The circumference of this rectangle is %.3f cm.\n(Width x 2 + Height x 2)\n"%(sum(side)*2)
    text += "All four corners of a rectangle are right angles (90°)."
    return text

def info_circ(radius):
    """Infro of the circle"""
    text = "The area of this circle is %.3f sqcm.\n(π x r^2)\n"%(pi * radius ** 2)
    text += "The circumference of this circle is %.3f cm.\n(2 x π x r)\n"%(2 * pi * radius)
    return text

def info_ell(radius):
    """Info of the radius"""
    text = "The area of this ellipse is %.3f sqcm.\n(π x a x b)\n"%(pi * radius[0] * radius[1])
    text += "The approximate circumference of this "
    text += "ellipse is %.3f cm.\n(2 x π x √((a^2 + b^2)/2))\n"%(2 * pi * sqrt((radius[0]**2 + radius[1]**2)/2))
    return text

def repeat():
    """Run this code again"""
    screen.clear()
    main()

main()

#Keep the programme running until closing the windows.
top = tk.Tk()
top.title("Calculate Again?")
top.geometry("300x50")
b = tk.Button(top,text = "Again", command = repeat)
b.pack()
top.mainloop()
screen.mainloop()
root.mainloop()
