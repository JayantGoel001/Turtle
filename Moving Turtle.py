import turtle as t
import random as rd


def inside_window():
    left_limit = -t.window_width() / 2 + 100
    right_limit = t.window_height() / 2 - 100

    top_limit = t.window_height() / 2 - 100
    bottom_limit = -t.window_height() / 2 + 100

    x, y = t.pos()
    return left_limit < x < right_limit and bottom_limit < y < top_limit


def move_turtle():
    dist = rd.randint(50, 250)
    if inside_window():
        t.right(angle=rd.randint(0, 180))
        t.forward(dist)
    else:
        t.backward(dist)


wn = t.getscreen()
wn.bgcolor("black")

t.shape('turtle')
t.fillcolor("white")
t.speed('slow')

while True:
    move_turtle()

wn.mainloop()
