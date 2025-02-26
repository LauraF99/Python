try:
    n1 = 16
    n2 = int(input("Digite outro número: "))
    resultado = n1/n2

except ZeroDivisionError:
    print("Erro: não é possível dividir por zero")
else:
    print(resultado)
    
