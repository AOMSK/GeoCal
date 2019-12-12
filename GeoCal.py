"""
Geometric Shape Calculator
A calculator and graphic representator for geometric shapes.

Created By
62070025 Janisda Mukda
62070088 Tawatchai Hanon
62070124 Piyaporn Phutpore
62070196 Sipang Klinhom
"""

import turtle
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
mylist = tk.Listbox(root, yscrollcommand=scrollbar.set, width=int(w_px / 10))

print("Geometric Calculator")
print("Shapes currently supported:\nSquares\nRectangles\nParallelograms\nTrapezoids\nTriangles\nCircles\nEllipses\nPolygons\nArcs")
print("Shapes too large will be resized to fit the screen but the calculations will still used the input given.")
print("Please input the shape name in singular form.")

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
    shapelist = {"square": square, "rectangle": recta, "trapezoid": trapezoid, "circle": circle,
                 "parallelogram": parallelogram, "triangle": triangle, "ellipse": ellipse, "polygon": poly, "arc": draw_arc}
    try:
        shape = shape.lower()
        mylist.insert(tk.END, "Shape input: %s" % shape)
        info = shapelist[shape](bob)
        bob.hideturtle()
        shape_info(shape, info)
    except AttributeError as exception:
        cancel()
    except KeyError:
        mylist.insert(tk.END, "%s is an invalid Shape, or Shape not supported"%shape)
        mylist.insert(tk.END, "\n")
        mylist.pack()
        repeat()

#Quadrilaterals
def square(t):
    """Draw a square"""
    lenght = turtle.textinput("Please input the size", "in cm")
    resized_size = 1
    if lenght == None:
        cancel()
        return
    if incorrect(lenght, 0):
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
    _polygon_(t, 4, lenghtpx)
    reference(resized_size)
    return lenght

def recta(t):
    """Draw a quadrilateral"""
    sides = turtle.textinput("Please input the size in cm", "sides1 sides2")
    resized_size = 1
    if sides == None:
        cancel()
        return
    if incorrect(sides, 1):
        sides = [5, 10]
        mylist.insert(tk.END, "DIDN'T INPUT THE REQUIRED VALUE(S), USING THE DEFAULT VALUE(S)")
    else:
        sides = [float(i) for i in sides.split()]
    mylist.insert(tk.END, scatter(sides))
    sidespx = [i*px_cm for i in sides]
    ratio = sidespx[0] / sidespx[1] #will be used if input is too large to draw
    if any([sidespx[0] > w_px//2, sidespx[1] > w_px//2]):
        sidespx = [(w_px/3)*ratio, w_px/3]
        mylist.insert(tk.END, "Input too large: drawing resized")
        resized_size = (sides[1] * px_cm) / sidespx[1]
    t.penup()
    t.setpos(-(sidespx[0]/2), -(sidespx[1]/2))
    t.pendown()
    for _ in range(2):
        t.fd(sidespx[0])
        t.lt(90)
        t.fd(sidespx[1])
        t.lt(90)
    reference(resized_size)
    return sides

def trapezoid(t):
    """Draw trapezoid"""
    #enter trapezoid parts
    sides = turtle.textinput("Enter the sides:", "Base_A Base_B Leg_A Leg_B Height")
    if sides == None:
        cancel()
        return
    if incorrect(sides, 4):
        sides = [10, 9, 9, 8, 7]
        mylist.insert(tk.END, "DIDN'T INPUT THE REQUIRED VALUE(S), USING THE DEFAULT VALUE(S)")
    else:
        sides = [float(i) for i in sides.split()]
    mylist.insert(tk.END, scatter(sides))
    base_a = sides[0] * px_cm
    base_b = sides[1] * px_cm
    leg_a = sides[2] * px_cm
    leg_b = sides[3] * px_cm
    height = sides[4] * px_cm
    #find base angles
    angles_1 = degrees(asin(height / leg_a))
    angles_2 = degrees(acos(height / leg_b))
    #Turtle
    t.fd(max(base_a, base_b))
    t.lt(90+(90-angles_1))
    t.fd(leg_a)
    t.lt(angles_1)
    t.fd(min(base_a, base_b))
    t.lt(90-angles_2)
    t.fd(leg_b)
    return sides + [angles_1, angles_2]

def parallelogram(t):
    """#Draw a parallelogram"""
    sides = turtle.textinput("Please input the sides in cm", "base height vertical sides")
    if sides == None:
        cancel()
        return
    if incorrect(sides, 2):
        sides = [8, 5, 6]
        mylist.insert(tk.END, "DIDN'T INPUT THE REQUIRED VALUE(S), USING THE DEFAULT VALUE(S)")
    else:
        sides = [float(i) for i in sides.split()]
    sidespx = [i * px_cm for i in sides]
    sine = sides[1] / sides[2]
    lesser_angle = degrees(asin(sine))
    for _ in range(2):
        t.forward(sidespx[0])
        t.lt(180-(180-lesser_angle))
        t.forward(sidespx[1])
        t.lt(180-lesser_angle)
    text = info_parall(sides)
    return sides

#Triangles
def triangle(t):
    """Draw a triangle"""
    sides = turtle.textinput("Please input the 3 sides in cm.", "A B C")
    resized_size = 1
    if sides == None:
        cancel()
        return
    if incorrect(sides, 2):
        sides = [5, 5, 5]
        mylist.insert(tk.END, "DIDN'T INPUT THE REQUIRED VALUE(S), USING THE DEFAULT VALUE(S)")
    else:
        sides = [float(i) for i in sides.split()]
    mylist.insert(tk.END, scatter(sides))
    sidespx = [i*px_cm for i in sides]
    angle_A = degrees(acos((sides[1]**2 + sides[2]**2 - sides[0]**2)/(2*sides[1]*sides[2])))
    angle_B = degrees(acos((sides[2]**2 + sides[0]**2 - sides[1]**2)/(2*sides[2]*sides[0])))
    angle_C = degrees(acos((sides[0]**2 + sides[1]**2 - sides[2]**2)/(2*sides[0]*sides[1])))
    t.penup()
    t.setpos(-(sidespx[0]/2), -(sidespx[1]/2))
    t.pendown()
    t.fd(sidespx[0])
    t.lt(180-angle_C)
    t.fd(sidespx[1])
    t.lt(180-angle_A)
    t.fd(sidespx[2])
    reference(resized_size)
    return sides + [angle_A, angle_B, angle_C]

#Ovals
def circle(t):
    """Draw a circle of a certain radius"""
    radius = turtle.textinput("Please input the radius", "in cm")
    resized_size = 1
    if radius == None:
        cancel()
        return
    if incorrect(radius, 0):
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
    _arc_(t, radiuspx)
    reference(resized_size)
    return radius

def ellipse(t):
    """Draw an ellipse"""
    radius = turtle.textinput("Please enter the radiuses", "Minor Major\nin cm")
    resized_size = 1
    if radius == None:
        cancel()
        return
    if incorrect(radius, 1):
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
    _arc_(t, radiuspx[1]/3, 90)
    _arc_(t, radiuspx[0]/3, 90)
    _arc_(t, radiuspx[1]/3, 90)
    _arc_(t, radiuspx[0]/3, 90)
    reference(resized_size)
    return radius

#Polygon
def poly(t, side_num=6):
    """Draw a square"""
    lenght = turtle.textinput("Please input these values:", "lenght in cm and the number of edges")
    resized_size = 1
    if lenght == None:
        cancel()
        return
    if incorrect(lenght, 1):
        lenght = 10
        mylist.insert(tk.END, "DIDN'T INPUT THE REQUIRED VALUE(S), USING THE DEFAULT VALUE(S)")
    else:
        lenght = lenght.split()
        side_num = int(lenght[1])
        lenght = float(lenght[0])
    mylist.insert(tk.END, "%.2f, %d" % (lenght, side_num))
    if side_num < 3:
        mylist.insert(tk.END, "THERE IS NO POLYGON WITH %d SIDES." % side_num)
        return
    lenghtpx = lenght * px_cm
    if (lenghtpx * side_num / pi) > h_px:
        lenghtpx = (h_px * 90/100) * pi / side_num
        mylist.insert(tk.END, "Input too large: drawing resized")
        resized_size = (lenght * px_cm) / lenghtpx
    t.penup()
    t.setpos(-(lenghtpx/2), -((lenghtpx * side_num / pi) / 2))
    t.pendown()
    _polygon_(t, side_num, lenghtpx)
    reference(resized_size)
    return lenght, side_num

def draw_arc(t):
    """Draw an arc with turtle"""
    angr =turtle.textinput("Please input these values:", "Angle Radius")
    resized_size = 1
    if angr == None:
        cancel()
        return
    if incorrect(angr, 1):
        angr = [90, 10]
        mylist.insert(tk.END, "DIDN'T INPUT THE REQUIRED VALUE(S), USING THE DEFAULT VALUE(S)")
    else:
        angr = [float(i) for i in angr.split()]
    angle, radius = angr[0], angr[1] * px_cm / 3
    if radius > h_px // 2:
        radius = h_px // 3
        resized_size = angr[1] / radius
    _arc_(t, radius, angle)
    reference(resized_size)
    return angr

#Draw the lines
def _arc_(t, radius=50, angle=360.0):
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

def _polygon_(t, side=6, lenght=100):
    """Draw a _polygon_ of a certain side lenght and edges"""
    angle = 360.0/side
    polyline(t, side, lenght, angle)

#Shows the infomations
def shape_info(name, shape_data):
    """Output the calculations"""
    if name == None or shape_data == None:
        mylist.pack()
        return
    info_dict = {"square": info_sq, "rectangle": info_rect, "trapezoid": info_trap, "circle": info_circ,
                 "parallelogram": info_parall, "triangle": info_tri, "ellipse": info_ell, "polygon": info_poly, "arc": info_arc}
    data = info_dict[name](shape_data)
    data = data.split("|")
    for i in data:
        mylist.insert(tk.END, i)
    mylist.insert(tk.END, "\n")
    mylist.pack()

def info_sq(side):
    """Info of the square"""
    text = "The area of this square is %.3f sqcm.  (Side^2)|"%(side**2)
    text += "The perimeter of this square is %.3f cm  (Side x 4)|"%(side*4)
    text += "All four corners of a square are right angles (90°)."
    return text

def info_rect(side):
    """Info of the rectangle"""
    text = "The area of this rectangle is %.3f sqcm.  (Width x Height)|"%(side[0] * side[1])
    text += "The perimeter of this rectangle is %.3f cm.  (Width x 2 + Height x 2)|"%(sum(side)*2)
    text += "All four corners of a rectangle are right angles (90°)."
    return text

def info_circ(radius):
    """Infro of the circle"""
    text = "The area of this circle is %.3f sqcm.  (π x r^2)|"%(pi * radius ** 2)
    text += "The circumference of this circle is %.3f cm.  (2 x π x r)    "%(2 * pi * radius)
    return text

def info_ell(radius):
    """Info of the ellipse"""
    text = "The area of this ellipse is %.3f sqcm.  (π x a x b)|" % (pi * radius[0] * radius[1])
    text += "The approximate circumference of this "
    text += "ellipse is %.3f cm.  (2 x π x √((a^2 + b^2)/2))" %(2 * pi * sqrt((radius[0]**2 + radius[1]**2) / 2))
    return text

def info_tri(side_and_angles):
    """Info of the triangles"""
    text = "The perimeter of this triangle is %.2f cm.  (P = a + b + c)  |" %(side_and_angles[0] + side_and_angles[1] + side_and_angles[2])
    text += "The angle A is %.2f° degrees.  (b**2 + c**2 - a**2)/(2*b*c)|" %side_and_angles[3]
    text += "The angle B is %.2f° degrees.  (c**2 + a**2 - b**2)/(2*c*a)|" %side_and_angles[4]
    text += "The angle C is %.2f° degrees.  (a**2 + b**2 - c**2)/(2*a*b)" %side_and_angles[5]
    return text

def info_trap(size):
    """Info of the trapezoid"""
    text = "The area of this trapezoid is %0.2f sqcm.|" % (1/2*(size[0] + size[1]) * size[4])
    text += "The perimeter of this trapezoid is %0.2f cm.|" % (size[0] + size[1] + size[2] + size[3])
    text += "All angles of this trapezoid from lower right to lower left, counter clockwise are:| %0.2f°, %0.2f°, %0.2f°, %0.2f°." % (size[5], 180 - size[5], size[6] + 90, 180 - (size[6] + 90))
    return text

def info_parall(side):
    """Info of the parallelogram"""
    text = "The area of this parallelogram is %.2f sqcm.  (base x Height)|" % (side[0] * side[1])
    text += "The perimeter of this parallelogram is %.2f cm.  (Sum of all the sides)" % ((side[0] * 2) + (side[2] * 2))
    return text

def info_poly(sides):
    """Info of polygons"""
    lenght, num = sides[0], sides[1]
    poly_name_dict = {3: "triangle", 4: "quadrilateral", 5: "penta", 6: "hexa", 7: "hepta", 8: "hexa", 9: "nona",
                      10: "deca", 11: "hendeca", 12: "dodeca"}
    poly_name = poly_name_dict.get(num) + ("gon" * (num > 4)) if num in poly_name_dict.keys() else "%d sided polygon" % num
    text = "This polygon is a(n) %s.|"%poly_name
    text += "It has a perimeter of %.2f cm|"%(lenght * num)
    text += "Each angles in this %s is %d°|"%(poly_name, 360 / num)
    return text

def info_arc(angr):
    """Info of arcs"""
    angle, radius = angr[0], angr[1]
    return "The lenght of this arc is %.2f cm" % (radius * 2 * pi * (angle / 360))

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
    ref.setpos(w_px//4 + px_cm, - (h_px//4))
    ref.write("%.2f cm"%num)
    ref.hideturtle()

def cancel():
    """Cancel the calculation"""
    mylist.insert(tk.END, "(cancelled)")
    mylist.insert(tk.END, "\n")
    scrollbar.config(command = mylist.yview)
    mylist.pack()

def incorrect(text, num):
    """Check if the input is in the correct format"""
    text = text.rstrip(" ")
    return text.count(" ") != num or any([not i.isdigit() and i != "." for i in text.replace(" ", "")])

main()

#Keep the programme running until closing the windows.
again_button = tk.Button(root, text="Calculate Again", command=repeat, bd=2)
exit_button = tk.Button(root, text="  Exit  ", command=exit, bd=2)
exit_button.pack(side=tk.RIGHT)
again_button.pack(side=tk.RIGHT, padx=1)
screen.mainloop()
root.mainloop()
