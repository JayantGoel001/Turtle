import turtle as t


def createBorder(length, breadth):
    for i in range(4):
        if i % 2 != 0:
            t.forward(length)
            t.right(90)
        else:
            t.forward(breadth)
            t.right(90)


def createRectangle(length, breadth, color):
    t.pendown()
    t.pensize(1)
    t.color(color)
    t.begin_fill()

    createBorder(length, breadth)

    t.end_fill()
    t.penup()


wn = t.getscreen()
t.bgcolor("black")
t.penup()
t.speed(5)

t.goto(-100, -150)
createRectangle(20, 50, "blue")

t.goto(-30, -150)
createRectangle(20, 50, "blue")

t.goto(-25, -50)
createRectangle(100, 15, "gray")

t.goto(-70, -50)
createRectangle(100, 15, "gray")

t.goto(-90, 100)
createRectangle(150, 100, "red")

t.goto(-150, 70)
createRectangle(15, 60, "gray")
t.goto(-150, 110)
createRectangle(40, 15, "gray")

t.goto(10, 70)
createRectangle(15, 60, "gray")
t.goto(55, 110)
createRectangle(40, 15, "gray")

t.goto(-50, 120)
createRectangle(20, 15, "gray")

t.goto(-85, 170)
createRectangle(50, 80, "red")

t.goto(-60, 160)
createRectangle(10, 30, "white")

t.goto(-55, 155)
createRectangle(5, 5, "black")
t.goto(-40, 155)
createRectangle(5, 5, "black")

t.goto(-65, 138)
createRectangle(5, 40, "black")
t.hideturtle()

wn.mainloop()
