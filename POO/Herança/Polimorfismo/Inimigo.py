class Inimigo():
    def __init__(self, nome, hp, dano):
        self.nome = nome
        self.hp = hp
        self.dano = dano
        
    def emitirSom(self):
        print('Inimigo', self.nome)
        
    def receberDano(self,dano):
        self.hp -= dano
        print(self.hp)
        if self.hp <= 0:
            print('Morreu :(')
        
class Lobo (Inimigo):
    def __init__(self, nome, hp, dano, escudo):
        super().__init__(nome,hp,dano)
        self.escudo = escudo
    
    def emitirSom(self):
        super().emitirSom()
        print('AUUUUUUUUuu!')
    
    def printStatus(self):
        print(self.hp)
        print(self.escudo)
        
    def receberDano(self, dano):
        if self.escudo > dano:
            self.escudo -= dano
            self.printStatus()    
        elif dano > self.escudo:
            self.escudo -= dano
            dano -= self.escudo
            return super().receberDano(dano)
        
            
        
lobo1 = Lobo('Alberto', 100, 50, 10)
lobo1.emitirSom()
lobo1.printStatus()
lobo1.receberDano(100)