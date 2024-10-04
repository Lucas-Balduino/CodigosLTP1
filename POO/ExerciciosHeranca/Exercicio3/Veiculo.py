class Veiculo:
    def __init__(self, modelo, marca, ano) -> None:
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        
    def descrever(self):
        print(f"Veiculo de modelo {self.modelo}, marca {self.marca} e ano de fabricação {self.ano}")
    
class Carro(Veiculo):
    def __init__(self,modelo,marca,ano):
        super().__init__(modelo,marca,ano)
    
    def descrever(self):
        print(f"Carro de modelo {self.modelo}, marca {self.marca} e ano de fabricação {self.ano}")
        
class Moto(Veiculo):
    def __init__(self,modelo,marca,ano):
        super().__init__(modelo,marca,ano)
    
    def descrever(self):
        print(f"Moto de modelo {self.modelo}, marca {self.marca} e ano de fabricação {self.ano}")
    
Carro1 = Carro('Onix','Chevrolet', 2014)
Moto1 = Moto('G 310 GS','BMW', 2020)

Carro1.descrever()
Moto1.descrever()