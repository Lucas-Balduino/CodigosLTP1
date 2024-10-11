'''Crie um programa que gerencie o banco de dados de uma 
biblioteca. O programa deve permitir adicionar um novo 
livro (como uma lista contendo título, autor e ano), 
listar todos os livros, e permitir a busca de livros
pelo título'''
# Array para armazenar os livros
biblioteca = []

# Função para adicionar um livro
def adicionar_livro(titulo, autor, ano):
    livro = [titulo, autor, ano] #Cria um array com as informacoes entregues pelo usuario
    biblioteca.append(livro) #Adiciona ao array de Livros
    print(f'Livro "{titulo}" adicionado com sucesso!') #Mensagem falando que adicionou o livro

# Função para listar todos os livros
def listar_livros():
    if biblioteca != []: # Se a biblioteca nao estiver vazia
        print("\nLista de livros:")
        for i in range(len(biblioteca)):
            print(f"{i}. Título: {biblioteca[i][0]}, Autor: {biblioteca[i][1]}, Ano: {biblioteca[i][2]}")
    else:
        print("\nNenhum livro na biblioteca.")

# Função para buscar um livro pelo título
def buscar_livro(titulo):
    encontrados = []
    for i in range(len(biblioteca)):
        if titulo == biblioteca[i][0]:
            encontrados.append(biblioteca[i])
    if encontrados != []:
        print("\nLivros encontrados:")
        for i in range(len(encontrados)):
             print(f"{i}. Título: {encontrados[i][0]}, Autor: {encontrados[i][1]}, Ano: {encontrados[i][2]}")
    else:
        print(f'\nNenhum livro com o título "{titulo}" encontrado.')

# Menu principal
def menu():
    while True:
        print("/////////////////////////////////")
        print("/////////////Menu////////////////")
        print("/////////////////////////////////")
        print("//          Insira:            //")
        print("//       1. Adicionar livro    //")
        print("//  2. Listar todos os livros  //")
        print("// 3. Buscar livro por título  //")
        print("//       4 - Sair              //")
        print("/////////////////////////////////")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            ano = input("Digite o ano de publicação: ")
            adicionar_livro(titulo, autor, ano)

        elif opcao == '2':
            listar_livros()

        elif opcao == '3':
            titulo = input("Digite o título do livro para buscar: ")
            buscar_livro(titulo)

        elif opcao == '4':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o menu
menu()
