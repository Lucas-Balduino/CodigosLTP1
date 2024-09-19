from CarroClass import Carro


carro1 = Carro('Chevrolet', 'Camaro', 'Amarelo', 2024, 10000)

carro1.acelerar()
carro1.frenar()

print(carro1.getMarca())
print(carro1.getModelo())
print(carro1.getCor())
print(carro1.getAno())
print(carro1.getRodagem())

carro1.setMarca('Toyota')
carro1.setModelo('Corola')
carro1.setCor('Prata')
carro1.setAno(2020)
carro1.setRodagem(200000)

carro1.acelerar()
carro1.frenar()

print(carro1.getMarca())
print(carro1.getModelo())
print(carro1.getCor())
print(carro1.getAno())
print(carro1.getRodagem())