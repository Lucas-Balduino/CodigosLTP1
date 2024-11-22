import turtle as tl

for i in range(1000):
    tl.forward(20)
    tl.left(i)
    if i % 2 != 0:
        tl.color('blue')
    if i % 3 != 0:
        tl.color('green')
    if i % 5 != 0:
        tl.color('yellow')
