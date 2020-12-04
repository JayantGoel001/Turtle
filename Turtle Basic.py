import turtle as t

wn = t.getscreen()
wn.bgcolor("black")

t.color("white")
t.goto(-100, -100)
t.goto(100, -100)
t.goto(0, 0)

t.penup()
t.goto(0, 100)
t.pendown()

t.goto(100, 100)
t.goto(0, 150)
t.goto(-100, 100)
t.goto(0, 100)

t.speed(100)
t.pensize(5)
t.color("blue")

t.right(90)
t.forward(100)

wn.mainloop()
