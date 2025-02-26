class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def detalhes(self):
        print(f"Nome: {self.nome}")
        print(f"Salário: {self.salario:.2f}")
        
class Gerente (Funcionario):
    def aumento(self, funcionario, porcentagem):
        if porcentagem > 0:
            aumento = funcionario.salario * (porcentagem / 100)
            funcionario.salario += aumento
            print(f"Salário de {funcionario.nome} aumentado em {porcentagem}%. Novo salário: R${funcionario.salario:.2f}")
        else:
            print("A porcentagem de aumento deve ser maior que 0.")

func1 = Funcionario("Laura", 1500)
func2 = Funcionario("James", 1500)
gere1 = Gerente("Andre", 4500)

func1.detalhes()
func2.detalhes()
print()
gere1.aumento(func1,20)
print()
func1.detalhes()
func2.detalhes()