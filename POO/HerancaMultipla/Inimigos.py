class NPC:
    def __init__(self, nome, gold):
        self.nome = nome
        self.gold = gold
    
    def falar (self):
        print('Olá, bem-vindo!')
        
class Inimigo:
    def __init__(self, nome, hp, dano):
        self.nome = nome
        self.hp = hp
        self.dano = dano
    
    def falar (self):
        print('>:(')
        
class Personagem(NPC,Inimigo): #Ordem dos atributos importa, o primeiro sera acessado antes
    def __init__(self, nome, gold, hp, dano):
        NPC.__init__(self,nome, gold)
        Inimigo.__init__(self,nome,hp,dano)

    def falar(self):
        NPC.falar(self)
        Inimigo.falar(self)
        #super().falar() - Chama a funcao do NPC, mais prioridade
        
personagem1 = Personagem ('Pedrinho', 1000, 100, 10)
print(personagem1.nome)
personagem1.falar()