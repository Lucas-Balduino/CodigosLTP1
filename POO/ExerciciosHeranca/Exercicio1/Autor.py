class Livro:
    def __init__(self, titulo, ano, autor):
        self.titulo = titulo
        self.ano = ano
        self.autor = autor
    
    def livroInfo(self):
        print(f'Título: {self.titulo}, 'f'Ano de Lançamento: {self.ano}, 'f'Autor: {self.autor.nome}')
        
livro1 = Livro('Memórias Póstumas de Brás Cubas', 1881, 'Machado de Assis')

livro1.livroInfo()
    
        
    
    