#Não compreendi essa atividade
class Veiculo:
    def tipo(self):
        return "Veículo"

class Carro(Veiculo):
    def tipo(self):
        return "Carro"

class Moto(Veiculo):
    def tipo(self):
        return "Moto"


carro = Carro()
moto = Moto()

print(carro.tipo()) 