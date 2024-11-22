import turtle as tl
tl.color('#0078D0')#Azul
tl.pensize(10)
#Desenho Olimpiadas
tl.tracer(0,0)

tl.up()

tl.setposition(-220,0)

tl.down()

for i in range(120):
    tl.forward(5)
    tl.left(3)

tl.up()

tl.setposition(-110,-90)

tl.down()

tl.color('#FFB114')#Amarelo

for i in range(120):
    tl.forward(5)
    tl.left(3)

tl.up()

tl.setposition(0,0)

tl.color('black')

tl.down()

for i in range(120):
    tl.forward(5)
    tl.left(3)

tl.up()

tl.setposition(110,-90)

tl.color('#00A651')#Verde

tl.down()

for i in range(120):
    tl.forward(5)
    tl.left(3)

tl.up()

tl.setposition(220,0)

tl.color('#F0282D')#Vermelho

tl.down()

for i in range(190):
    tl.forward(5)
    tl.left(3)

tl.done()
