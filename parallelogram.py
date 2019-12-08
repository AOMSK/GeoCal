"""parallelogram"""
import turtle
"""pal = turtle.Turtle()
pal.forward(150)
pal.right(110)
pal.forward(90)
pal.right(70)
pal.forward(150)
pal.right(110)
pal.forward(90)"""

def parallelogram():
    """#Draw Parallelogram"""
    side = turtle.Turtle()
    side = turtle.textinput("Please input the size in cm", "base side")
    side = [float(i) for i in side.split()]
    for _ in range(2):
        t.forward(side[0])
        t.right(110)
        t.forward(side[1])
        t.right(70)
    return side
parallelogram()
