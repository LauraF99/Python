class Aluno:
    def __init__(self,nome,nota):
        self.nome = nome
        self.nota = nota
    
    def avaliar (self):
        if self.nota >= 7:
            print(f"{self.nome} foi aprovado(a)")
        else:
            print(f"{self.nome} foi reprovado(a)") 
            
aluno1 = Aluno("Laura", 8)
aluno1.avaliar()