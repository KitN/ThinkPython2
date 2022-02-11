import turtle

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)

def koch(t, length):
    print('calling with ', length)
    if length < 10:
        t.fd(length)
        return
    koch(t, length/3)
    t.lt(90)
    koch(t, length/3)
    t.rt(180)
    koch(t, length/3)
    t.lt(90)
    koch(t, length/3)
    # Something to return to the starting angle?

def snowflake(t, length):
    koch(t, length)
    t.rt(120)
    koch(t, length)
    t.rt(120)
    koch(t, length)

bob = turtle.Turtle()

snowflake(bob, 250)
turtle.mainloop()
