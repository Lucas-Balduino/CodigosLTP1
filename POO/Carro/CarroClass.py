from typing import Any


class Carro():
    def __init__(self, marca, modelo, cor, ano, rodagem): #Metodo Contrutor dessa classe (Definicao de Atributos) - (Nome padrao de Metodo contrutor)
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.rodagem = rodagem

    def acelerar(self):
        print("Vrummmm")
    
    def frenar(self):
        print("Carro Desacelerando")

    #Metodos get para acessar atributos privados
    def getModelo(self):
        return self.modelo

    def getMarca(self):
        return self.marca

    def getCor(self):
        return self.cor

    def getAno(self):
        return self.ano

    def getRodagem(self):
        return self.rodagem

    #Metodos set para definir atributos privados
    def setMarca(self, novaMarca):
        self.marca = novaMarca
        return novaMarca
     
    def setModelo(self, novoModelo):
        self.modelo = novoModelo
        return novoModelo
     
    def setCor(self, novaCor):
        self.cor = novaCor
        return novaCor
     
    def setAno(self, novoAno):
        self.ano = novoAno
        return novoAno
     
    def setRodagem(self, novaRodagem):
        self.rodagem = novaRodagem
        return novaRodagem 