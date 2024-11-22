class Livro:
    def __init__(self, titulo, ano, autor):
        self.__titulo = titulo
        self.__ano = ano
        self.__autor = autor
        
    @property
    def titulo(self):
        return self.__titulo
    
    @titulo.setter
    def titulo(self,titulo):
        self.__titulo = titulo
    
    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self,ano):
        self.__ano = ano
    @property
    def autor(self):
        return self.__autor
    
    @autor.setter
    def autor(self,autor):
        self.__autor = autor
    

livro1 = Livro('Memórias Póstumas de Brás Cubas', 1881, 'Machado de Assis')
print(livro1.titulo)
print(livro1.ano)
print(livro1.autor)
livro1.titulo = "Dom Casmurro"
print(livro1.titulo)
livro1.ano = 1899
print(livro1.ano)
livro1.autor = "Machado de Assis"
print(livro1.autor)
    
        
    
    