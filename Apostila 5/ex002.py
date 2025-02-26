class Livro:
    def __init__(self,titulo, autor):
        self.titulo = titulo
        self.autor = autor
    
    def detalhes(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        

livro1 = Livro("O pequeno príncipe","Antoine de Saint-Exupéry")
livro2 = Livro("Senhora", "José de Alencar")

livro1.detalhes()
print()
livro2.detalhes()

    
    