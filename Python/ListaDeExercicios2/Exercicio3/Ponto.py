'''
    Implemente uma classe Ponto com um construtor que aceita coordenadas x e y como atributos. 
    Utilize o objeto ponto como parâmetro para o comando goto() da Turtle.
'''
import turtle as tl
class Ponto():
    def __init__(self, x,y):
        self.x = x
        self.y = y

ponto = Ponto(100,100)

tl.goto(ponto.x,ponto.y)

tl.done()
