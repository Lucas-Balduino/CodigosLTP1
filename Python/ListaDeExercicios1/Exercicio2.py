'''Dada a tupla turma = ('André', 'Fernanda', 'Luiz'), 
peça ao usuário para digitar o nome de um aluno. Cheque
se o aluno está na tupla e exiba uma mensagem adequada.'''

turma = ('André', 'Fernanda', 'Luiz') #Declaracao da tupla

nomeDeAluno = input("Digite o nome de um Aluno:") #Entrada de Dados

encontrado = False

#For para varrer a lista
for nome in turma:
    #Estrutura de Decisao: Está ou nao na lista
    if  nomeDeAluno == nome: #Se o nome inserido for igual ao nome do indice i 
        print(f"O Aluno {nomeDeAluno} está na lista!")
        encontrado = True
        break

#Se o nome inserido nao for igual
if not encontrado:
    print(f"O Aluno {nomeDeAluno} não está na lista!")