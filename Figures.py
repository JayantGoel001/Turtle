import turtle as t

wn = t.getscreen()
wn.bgcolor("black")
t.pencolor("white")

t.penup()
t.goto(-250, 250)
t.pendown()

t.forward(500)

t.right(90)
t.forward(500)

t.right(90)
t.forward(500)

t.right(90)
t.forward(500)

t.penup()
t.goto(-100, 100)
t.pendown()

for i in range(4):
    t.right(90)
    t.forward(200)

t.color("red")
t.penup()
t.goto(90, 0)
t.pendown()
t.speed(100)

for i in range(1, 90):
    t.circle(i)

t.color("blue")
config = {
    0: (-250, -250),
    1: (-250, 250),
    2: (250, -250),
    3: (250, 250)
}
for i in range(4):
    t.penup()
    t.goto(config[i])
    t.pendown()

    for j in range(10):
        t.circle(50)
        t.left(36)

config2 = {
    0: (-500, -250),
    1: (500, -250)
}
t.color("green")
t.pensize(2)

for i in range(2):
    t.penup()
    t.goto(config2[i])
    t.pendown()
    for j in range(5):
        t.forward(50)
        t.left(145)

config3 = {
    0: (-500, 250),
    1: (500, 250)
}

t.color("purple")

for i in range(2):
    t.penup()
    t.goto(config3[i])
    t.pendown()
    for j in range(10):
        t.forward(50)
        t.left(135)


wn.mainloop()
