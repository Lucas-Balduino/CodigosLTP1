class Paciente:

    def __init__(self,nome,idade,cpf): #Um metodo construtor
        self.nome = nome #Publico
        self._idade = idade #Protected
        self.__cpf = cpf #Private
        
    @property
    def cpf(self):
        return self.__cpf
    
    @cpf.setter
    def cpf(self,cpf):
        self.__cpf = cpf
    
    def getIdade(self):
        return self._idade
    
    def setIdade(self, idade):
        if idade > 0:
        	self._idade = idade
    
    