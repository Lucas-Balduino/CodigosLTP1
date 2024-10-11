'''
    Crie uma classe base Forma com um método desenhar() que desenha uma forma qualquer utilizando a biblioteca Turte. 
    Em seguida, crie subclasses Círculo e Quadrado que herdam de Forma e sobrescrevem desenhar() para desenhar as formas específicas.
'''

class Forma:
    def __init__(self,lado):
        self.lado = lado