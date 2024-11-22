'''
    É uma classe que não pode ser instanciada e destina-se a ser uma 
    classe base para outras subclasses.
'''

#Importar uma forma de abstrair a calsse por uma biblioteca

from abc import ABC, abstractmethod

#Classe abstrata

class FormaGeometrica(ABC):
    @abstractmethod
    def area(self):
        #Calcula a área da forma geométrica
        pass
    
    @abstractmethod
    def perimetro(self):
        #Calcula o perímetro da forma geométrica
        pass
    
#Subclasse Concreta
class Retangulo(FormaGeometrica):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    def area (self):
        return self.largura * self.altura
    
    def perimetro(self):
        return 2* (self.largura + self.altura)
    
class Circulo (FormaGeometrica):
    def __init__(self, raio):
        self.raio = raio
    
    def area(self):
        return 3.14 * (self.raio ** 2)
    
    def perimetro(self):
        return 2 * 3.14 * self.raio
    
try:
    forma = FormaGeometrica()

except Exception as e:
    print(e)
    
retangulo1 = Retangulo(4,5)
print(retangulo1.area())
print(retangulo1.perimetro())
circulo1 = Circulo(5)
print(circulo1.area())
print(circulo1.perimetro())
