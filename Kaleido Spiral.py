import turtle as t
from itertools import cycle

colors = cycle(["red", "green", "yellow", "gray", "blue", "pink", "white", "purple", "orange"])


def createCircle(rad, angle, forward):
    t.pencolor(next(colors))
    t.circle(radius=rad)
    t.right(angle)
    t.forward(forward)
    createCircle(rad + 5, angle + 1, forward + 1)


wn = t.getscreen()
t.bgcolor("black")
t.speed(10)
t.pensize(4)

createCircle(30, 0, 1)

wn.mainloop()
