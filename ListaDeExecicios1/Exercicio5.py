'''Escreva um programa que jogue "pedra, papel ou tesoura" 
contra o usuário. O jogo deve continuar até o usuário escolher
parar, e retornar o número de vitórias do usuário, da máquina, 
e empates..'''

import random

escolha = 0
contadorEmpate = 0
contadorVitoria = 0
contadorDerrota = 0

while escolha != -1:
    
#Gerador da escolha do Computador
    probabilidade = random.randint(1,100)
    print(probabilidade)
    if probabilidade < 34:
        escolhaComputador = 1
    elif probabilidade < 67:
        escolhaComputador = 2
    else:
        escolhaComputador = 3

#Interface de Escolha
    print("/////////////////////////////////")
    print("//Jogo de Pedra Papel e Tesoura//")
    print("/////////////////////////////////")
    print("//          Insira:            //")
    print("//        1 - Pedra            //")
    print("//        2 - Papel            //")
    print("//        3 - Tesoura          //")
    print("//       -1 - Sair             //")
    print("/////////////////////////////////")

#Entrada de Dados
    escolha = int(input())

#Casos de Empate
    
    if (escolhaComputador == 1 and escolha == 1):
        print("O computador tambem escolheu Pedra!")
        print("Voces Empataram!")
        contadorEmpate +=1
    if (escolhaComputador == 2 and escolha == 2):
        print("O computador tambem escolheu Papel!")
        print("Voces Empataram!")
        contadorEmpate +=1
    if (escolhaComputador == 3 and escolha == 3):
        print("O computador tambem escolheu Tesoura!")
        print("Voces Empataram!")
        contadorEmpate +=1

#Casos de Derrota
    if (escolhaComputador == 1 and escolha == 3):
        print("O computador escolheu Pedra!")
        print("Pedra ganha de Tesoura!")
        print("Voce Perdeu!")
        contadorDerrota +=1
    if (escolhaComputador == 2 and escolha == 1):
        print("O computador escolheu Papel!")
        print("Papel ganha de Pedra!")
        print("Voce Perdeu!")
        contadorDerrota +=1
    if (escolhaComputador == 3 and escolha == 2):
        print("O computador escolheu Tesoura!")
        print("Tesoura ganha de Papel!")
        print("Voce Perdeu!")
        contadorDerrota +=1

#Casos de Vitoria
    if (escolha == 1 and escolhaComputador == 3):
        print("O computador escolheu Tesoura!")
        print("Pedra ganha de Tesoura!")
        print("Voce Ganhou!")
        contadorVitoria +=1
    
    if (escolha == 2 and escolhaComputador == 1):
        print("O computador escolheu Pedra!")
        print("Papel ganha de Pedra!")
        print("Voce Ganhou!")
        contadorVitoria +=1
    
    if (escolha == 3 and escolhaComputador == 2):
        print("O computador escolheu Papel!")
        print("Tesoura ganha de Papel!")
        print("Voce Ganhou!")
        contadorVitoria +=1

print(f"Voce ganhou {contadorVitoria} vezes!")
print(f"Voce perdeu {contadorDerrota} vezes!")
print(f"Voce empatou {contadorEmpate} vezes!")