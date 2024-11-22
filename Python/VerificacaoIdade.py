#Codigo para verificacao de idade

idade = int(input('Digite sua idade: '))

if idade >= 0 and idade <= 3:
    print('Você é um bebe')

elif idade >= 4 and idade <= 11:
    print('Você é uma criança')

elif idade >= 12 and idade <= 17:
    print('Você é um adolescente')

elif idade >= 18 and idade <= 60:
    print('Você é Adulto')

elif idade >= 60:
    print('Você é idoso')

else:
    print('Idade Invalida')