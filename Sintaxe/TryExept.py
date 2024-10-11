try:
    #Codigo que pode levar a uma exceção
    print('e'+2)
    
except Exception as e:
    #Código que será executaado se uma exceção ocorrer no bloco try
    print("Ocorreu um erro: ",e)
    
###################################################################
#Ex:

try:
    #Codigo que pode levar a uma exceção
    valor = int(input("Digite um número: "))
    resultado = 10 / valor
    
except Exception as e:
    #Código que será executaado se uma exceção ocorrer no bloco try
    print("Divisão por zero não é permitida: ",e)

###################################################################

try:
    #Codigo que pode levar a uma exceção
    dividendo = 10
    divisor = 0
    resultado = dividendo / divisor
    
except ValueError as e:
    #Código que será executaado se uma exceção ocorrer no bloco try
    print("Por Favor insira um número válido: ",e)
    
except ZeroDivisionError as e:
    #Código que será executaado se uma exceção ocorrer no bloco try
    print("Divisão por zero não é permitida: ",e)

###################################################################

try:
    #Codigo que pode levar a uma exceção
    dividendo = 10
    divisor = 0
    resultado = dividendo / divisor
    
except ValueError as e:
    #Código que será executaado se uma exceção ocorrer no bloco try
    print("Por Favor insira um número válido: ",e)
    
except ZeroDivisionError as e:
    #Código que será executaado se uma exceção ocorrer no bloco try
    print("Divisão por zero não é permitida: ",e)
    
else:
    #Roda caso nao caia em nenhuma exceção
    print("Voce digitou o numero ",valor,"e o resultado é",resultado)
    
finally:
    #Parte do codigo que roda de qualuquer forma
    print("Esta mensagem sera umpressa nao importa o que aconteça")