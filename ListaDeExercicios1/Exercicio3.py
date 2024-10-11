'''Escreva um programa que imprima os primeiros 10
números da sequência de Fibonacci.'''

fibonacciList = [0,1] #Primieros dois itens da sequencia
#

for i in range(1,9,1):
    fibonacciNumber = fibonacciList[i] + fibonacciList[i-1] #Proximo numero da Lista = i + i - 1
    fibonacciList.append(fibonacciNumber) #Acrescentando o Proximo numero na Lista

print(fibonacciList)#Print da Lista com os 10 primeiros numeros
