'''
    Crie classes Motor, Pneu, Veiculo, onde Veiculo herda tanto de Motor quanto de Pneu. 
    Ambas as classes base (Motor e Pneu) devem ter um método chamado status() que retorna uma string. 
    A classe Veiculo deve também ter um método status() que chama os métodos status() das classes base. 
    Implemente a herança de modo que a classe Veiculo resolva o método status() de maneira correta.
'''
class Motor():
    def status(self):
        print("Vrum Vrum!")
        print("Motor Funcionando!")

class Pneu():
    def status(self):
        print("IIIIII!(Barulho de Pneu)")
        print("Pneus em bom estado")

class Veiculo(Motor,Pneu):
    def status(self):
        Motor.status(self)
        Pneu.status(self)
        print("Que Carrão!")

veiculo = Veiculo()
veiculo.status()