class Autor:
    def __init__(self, nome, pais, nascimento):
        self.nome = nome
        self.pais = pais
        self.nascimento = nascimento
        
    def autorInfo(self):
        print(f'Nome: {self.nome}, 'f'País: {self.pais}, 'f'Ano de Nascimento: {self.nascimento}')
        
class Livro:
    def __init__(self, titulo, ano, autor):
        self.titulo = titulo
        self.ano = ano
        self.autor = autor
    
    def livroInfo(self):
        print(f'Título: {self.titulo}, 'f'Ano de Lançamento: {self.ano}, 'f'Autor: {self.autor.nome}')
        
autor1 = Autor('Machado de Assis','Brasil', 1839)

livro1 = Livro('Memórias Póstumas de Brás Cubas', 1881, autor1)

livro1.livroInfo()
livro1.autor.autorInfo()
    
        
    
    