import turtle as tl

#tl.tracer()

tl.penup()
tl.setposition(-150,-150)
tl.pendown()

tl.pensize(10)

#Quadrado casa
for i in range(4):
    tl.begin_fill()
    tl.forward(300)
    tl.left(90)
    tl.end_fill()

tl.fillcolor()

tl.penup()

tl.setposition(-100,-30)

tl.pendown()

tl.pencolor('brown')

#Janela
tl.begin_fill()
for i in range(4):
    tl.forward(80)
    tl.left(90)

tl.end_fill()

tl.fillcolor('brown')

tl.penup()

tl.setposition(30,-150)

tl.pendown()

tl.pencolor('brown')

#Porta
tl.begin_fill()
tl.forward(90)
tl.left(90)
tl.forward(200)
tl.left(90)
tl.forward(90)
tl.left(90)
tl.forward(200)
tl.left(90)
tl.end_fill()

tl.fillcolor()

tl.penup()

tl.setposition(-150,150)

tl.pendown()

tl.pencolor('black')

#Telhado
tl.begin_fill()
tl.left(40)
tl.forward(195)
tl.right(80)
tl.forward(195)
tl.end_fill()

#tl.done()
