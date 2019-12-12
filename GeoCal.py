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
scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, activebackground="#00ffff")
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
mylist = tk.Listbox(root, yscrollcommand=scrollbar.set, width=int(w_px/10))
#root.maxsize(int(w_px//1.5), int(h_px//1.5))
print("Geometric Calculator")
print("Shapes currently supported:\nSquare\nRectangles\nCircles\nEllipses")
print("Shapes too large will be resized to fit the screen but the calculations will still used the input given.")

def main():
    """Main part of the programme.
    Works by taking an input, call the drawing functions,
    calculate the informations,
    then output the informations through tkinter."""
    screen.title("Graphic Representation")
    screen.screensize(w_px//2, h_px//2)
    shape = turtle.textinput("Geometric Shape Calculator", "Please input your desired shaped:")
    bob = turtle.Turtle()
    bob.delay = 1e-20 #set the turtle drawing speed
    shapelist = {"square": square, "circle": circle, "rectangle": recta, "ellipse": ellipse}
    try:
        shape = shape.lower()
        mylist.insert(tk.END, "Shape input: %s"%shape)
        info = shapelist[shape](bob)
        bob.hideturtle()
        shape_info(shape, info)
    except AttributeError as exception:
        cancel()
    except KeyError:
        mylist.insert(tk.END, "%s is an invalid Shape, or Shape not supported"%shape)
        mylist.insert(tk.END, "\n")
        repeat()

#Quadrilaterals
def square(t):
    """Draw a square"""
    lenght = turtle.textinput("Please input the size", "in cm")
    resized_size = 1
    if lenght == None:
        cancel()
        return
    if not re.match(r"\d", lenght):
        lenght = 10
        mylist.insert(tk.END, "DIDN'T INPUT THE REQUIRED VALUE(S), USING THE DEFAULT VALUE(S)")
    else:
        lenght = float(lenght)
    mylist.insert(tk.END, str(lenght))
    lenghtpx = lenght * px_cm
    if lenghtpx > h_px//2:
        lenghtpx = h_px/1.2
        mylist.insert(tk.END, "Input too large: drawing resized")
        resized_size = (lenght * px_cm) / lenghtpx
    t.penup()
    t.setpos(-(lenghtpx/2), -(lenghtpx/2))
    t.pendown()
    polygon(t, 4, lenghtpx)
    reference(resized_size)
    return lenght

def recta(t):
    """Draw a quadrilateral"""
    side = turtle.textinput("Please input the size in cm", "side1 side2")
    resized_size = 1
    if side == None:
        cancel()
        return
    if not re.match(r"(\d)(\w)(\d)", side):
        side = [5, 10]
        mylist.insert(tk.END, "DIDN'T INPUT THE REQUIRED VALUE(S), USING THE DEFAULT VALUE(S)")
    else:
        side = [float(i) for i in side.split()]
    mylist.insert(tk.END, scatter(side))
    sidepx = [i*px_cm for i in side]
    ratio = sidepx[0] / sidepx[1] #will be used if input is too large to draw
    if any([sidepx[0] > w_px//2, sidepx[1] > w_px//2]):
        sidepx = [(w_px/3)*ratio, w_px/3]
        mylist.insert(tk.END, "Input too large: drawing resized")
        resized_size = (side[1] * px_cm) / sidepx[1]
    t.penup()
    t.setpos(-(sidepx[0]/2), -(sidepx[1]/2))
    t.pendown()
    for _ in range(2):
        t.fd(sidepx[0])
        t.lt(90)
        t.fd(sidepx[1])
        t.lt(90)
    reference(resized_size)
    return side

#Ovals
def circle(t):
    """Draw a circle of a certain radius"""
    radius = turtle.textinput("Please input the radius", "in cm")
    resized_size = 1
    if radius == None:
        cancel()
        return
    if not re.match(r"\d", radius):
        radius = 5
        mylist.insert(tk.END, "DIDN'T INPUT THE REQUIRED VALUE(S), USING THE DEFAULT VALUE(S)")
    else:
        radius = float(radius)
    mylist.insert(tk.END, str(radius))
    radiuspx = radius * px_cm
    if radiuspx > h_px//2:
        radiuspx = w_px/4
        mylist.insert(tk.END, "Input too large: drawing resized")
        resized_size = (radius * px_cm) / radiuspx
    t.penup()
    t.setpos(0, -radiuspx,)
    t.pendown()
    arc(t, radiuspx)
    reference(resized_size)
    return radius

def ellipse(t):
    """Draw an ellipse"""
    radius = turtle.textinput("Please enter the radiuses", "Minor Major\nin cm")
    resized_size = 1
    if radius == None:
        cancel()
        return
    if not re.match(r"(\d)(\w)(\d)", radius):
        radius = [2, 3]
        mylist.insert(tk.END, "DIDN'T INPUT THE REQUIRED VALUE(S), USING THE DEFAULT VALUE(S)")
    else:
        radius = [float(i) for i in radius.split()]
    mylist.insert(tk.END, scatter(radius))
    radiuspx = [i*px_cm for i in radius]
    if any([radiuspx[0]/2 > h_px/4, radiuspx[1]/2 > w_px/4]):
        ratio = radiuspx[0] / radiuspx[1] #will be used if input is too large to draw
        radiuspx = [(w_px/6)*ratio, w_px/6]
        mylist.insert(tk.END, "Input too large: drawing resized")
        resized_size = (radius[1] * px_cm) / radiuspx[1]
    t.penup()
    t.setpos(-(radiuspx[1]), -(radiuspx[0]))
    t.pendown()
    t.rt(45)
    arc(t, radiuspx[1]/3, 90)
    arc(t, radiuspx[0]/3, 90)
    arc(t, radiuspx[1]/3, 90)
    arc(t, radiuspx[0]/3, 90)
    reference(resized_size)
    return radius

#Draw the lines
def arc(t, radius=50, angle=360.0):
    """Draw an arc"""
    side = int(angle/(radius/30)) + 20
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
    if name == None or shape_data == None:
        return
    info_dict = {"square": info_sq, "rectangle": info_rect, "circle": info_circ, "ellipse": info_ell}
    data = info_dict[name](shape_data).split("|")
    for i in data:
        mylist.insert(tk.END, i)
    mylist.insert(tk.END, "\n")
    mylist.pack()

def info_sq(side):
    """Info of the square"""
    text = "The area of this square is %.3f sqcm.  (Side^2)|"%(side**2)
    text += "The circumference of this square is %.3f cm  (Side x 4)|"%(side*4)
    text += "All four corners of a square are right angles (90°)."
    return text

def info_rect(side):
    """Info of the rectangle"""
    text = "The area of this rectangle is %.3f sqcm.  (Width x Height)|"%(side[0] * side[1])
    text += "The circumference of this rectangle is %.3f cm.  (Width x 2 + Height x 2)|"%(sum(side)*2)
    text += "All four corners of a rectangle are right angles (90°)."
    return text

def info_circ(radius):
    """Infro of the circle"""
    text = "The area of this circle is %.3f sqcm.  (π x r^2)|"%(pi * radius ** 2)
    text += "The circumference of this circle is %.3f cm.  (2 x π x r)    "%(2 * pi * radius)
    return text

def info_ell(radius):
    """Info of the radius"""
    text = "The area of this ellipse is %.3f sqcm.  (π x a x b)|"%(pi * radius[0] * radius[1])
    text += "The approximate circumference of this "
    text += "ellipse is %.3f cm.  (2 x π x √((a^2 + b^2)/2))    "%(2 * pi * sqrt((radius[0]**2 + radius[1]**2)/2))
    return text

def scatter(input_list):
    """Scatter the inputs into a string"""
    return " ".join([str(i) for i in input_list])

def repeat():
    """Run this code again"""
    screen.clear()
    main()
    scrollbar.config(command = mylist.yview)

def exit():
    """Exit the program"""
    print("Exiting the program.")
    root.destroy()
    screen.bye()

def reference(num):
    """Draw a size reference"""
    ref = turtle.Turtle()
    ref.penup()
    ref.setpos(w_px//4 + 2*px_cm, -(h_px//4 - 20))
    ref.lt(180)
    ref.pendown()
    ref.fd(px_cm)
    ref.penup()
    ref.setpos(w_px//4 + px_cm, -(h_px//4))
    ref.write("%.2f cm"%num)
    ref.hideturtle()

def cancel():
    """Cancel the calculation"""
    mylist.insert(tk.END, "(cancelled)")
    mylist.insert(tk.END, "\n")
    scrollbar.config(command = mylist.yview)
    mylist.pack()

main()

#Keep the programme running until closing the windows.
again_button = tk.Button(root, text="Calculate Again", command=repeat, bd=2)
exit_button = tk.Button(root, text="  Exit  ", command=exit, bd=2)
exit_button.pack(side=tk.RIGHT)
again_button.pack(side=tk.RIGHT, padx=1)
screen.mainloop()
root.mainloop()
