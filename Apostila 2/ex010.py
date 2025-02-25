velocidade = int(input("Digite a velocidade do carro em km/h: "))
tempo = int(input("Digite o tempo da viagem em horas: "))

distancia = velocidade * tempo

litrosUsados = round(distancia / 12, 2)

print(f"O seu carro com a velocidade média de {velocidade} km/h, durante {tempo} horas, percorreu {distancia} km")
print(f"Foram usados {litrosUsados} litros")