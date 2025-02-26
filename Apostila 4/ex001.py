while True:
    try:
        numero = int(input("Digite um número: "))
    except ValueError:
        print("Erro: Entrada inválida. Digite um número inteiro ")
    else:
        print(f"Você digitou {numero}")
        break
    
    
    




