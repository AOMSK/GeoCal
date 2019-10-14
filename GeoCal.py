"""
Geometric Shape Calculator
Created By
62070025 Janisda Mukda
62070088 Tawatchai Hanon
62070115 Parkorn Kampao
62070124 Piyaporn Phutpore
62070196 Sipang Klimhom
"""

import turtle
import tkinter as tk
from math import pi, sin, asin, radians, degrees
ROOT = tk.Tk()
W_PX = ROOT.winfo_screenwidth()
H_PX = ROOT.winfo_screenheight()
#Estimation of the amount of pixel in a 1 cm line in any direction
PX_CM = ((W_PX / (ROOT.winfo_screenmmwidth() / 10) + H_PX / (ROOT.winfo_screenmmheight() / 10)) / 2)

def main():
    """Main part of the program"""
    screen = turtle.Screen()
    screen.screensize(W_PX//2, H_PX//2)
    shape = turtle.textinput("Geometric Shape Calculator", "Please input your desired shaped:")
    shape = shape.lower()
    bob = turtle.Turtle()
    bob.delay = 0.00000000000000000000000000000000000001
    shapelist = {"square":square, "circle":circle, "rectangle":recta}
    info = shapelist[shape](bob)
    bob.hideturtle()
    shape_info(shape, info)
    screen.mainloop()

#Quadrilaterals
def square(t):
    """Draw a square"""
    lenght = turtle.textinput("Please input the size", "in cm")
    lenght = 10 if lenght == "" else float(lenght)*PX_CM
    polygon(t, 4, lenght)
    return lenght

def recta(t):
    """Draw a quadrilateral"""
    side = turtle.textinput("Please input the size in cm", "side1 side2")
    side = [float(i)*PX_CM for i in side.split()]
    for _ in range(2):
        t.fd(side[0])
        t.lt(90)
        t.fd(side[1])
        t.lt(90)

#Ovals
def circle(t):
    """Draw a circle of a certain radius"""
    radius = turtle.textinput("Please input the radius", "in cm")
    radius = 50 if radius == "" else float(radius)
    arc(t, radius)
    return radius

#Draw the lines
def arc(t, radius=50, angle=360.0):
    """Draw an arc"""
    side = int(angle//(radius//4)+10)
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
    info_dict = {"square":info_sq, "circle":info_circ}
    pen = turtle.Turtle()
    pen.penup()
    pen.fd(80)
    pen.rt(90)
    pen.fd(30)
    info_dict[name](pen, shape_data)
    pen.hideturtle()

def info_sq(pen, side):
    """Info of the square"""
    text = "The area of this square is %.3f sqcm\n (Side^2)\n"%(side**2)
    text += "The circumference of this square is %.3f cm\n (Side x 4)"%(side*4)
    pen.write(text, True, align="left")

def info_circ(pen, radius):
    """Info of the circle"""
    text = "The area of this circle is %.3f sqcm \n (Pi * R^2)\n"%(pi*radius**2)
    text += "The circumference of this circle is %.3f cm\n (2 x Pi x R)"%(2*pi*radius)
    pen.write(text, True, align="left")

main()
