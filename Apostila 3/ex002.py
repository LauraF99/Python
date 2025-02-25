def fatorial(n):
    f = 1
    for c in range(1, n + 1):
        f *= c
    return f        

n = int(input("Digite um número: "))
print(f"O fatorial de {n} é {fatorial(n)}")
