'''Exercício 1: Peça ao usuário que insira um número. 
Se o número for par, exiba "Número par". 
Se for ímpar, exiba "Número ímpar".'''

numero = int(input("Digite um Numero para saber se ele é par ou impar:")) #Entrada de Dados, tratamento para inteiro

#Estrutura de Decisao: Par ou Impar
if  numero % 2 == 0: #Se o resto da divisao for 0 o numero é par
    print(f"O numero {numero} é par")

else: #Se nao for 0 é impar
    print(f"O numero {numero} é impar")
