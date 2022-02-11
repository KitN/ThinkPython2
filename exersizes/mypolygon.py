import turtle
import math
bob = turtle.Turtle()

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)
def polygon(t, length, n):
    degrees = 360/n
    for i in range(n):
        t.fd(length)
        t.lt(degrees)
def circle(t, r):
    circumference = 2*3.14*r
    length = circumference / 30
    polygon(t, length, 30)

def arccircle(t, r, arc):
    percentage = arc/360
    circumference = 2*3.14*r
    length = circumference / 30
    polygon(t, length, int(30*percentage))

def drawpie(t, length, n):
    """ Draws an n-sided regular polygon pie
    t: which turtle
    r: radius
    n: number of sides
    """
    sinevalue = math.sin(math.pi/n)
    r = abs(length/(2*sinevalue))
    print(r)
    interior_angle = 180*(n-2)/n
    print(interior_angle)
    turning_angle = 360 / n
    # First draw a polygon
    polygon(t, length, n)
    # Then go to the centre
    t.lt(interior_angle/2)
    t.fd(r)
    for spoke in range(n-1):
        t.rt(180-(360/n))
        t.fd(r)
        t.rt(180)
        t.fd(r)

drawpie(bob, 100, 5)
bob.fd(200)
drawpie(bob, 69, 8)
turtle.mainloop()
