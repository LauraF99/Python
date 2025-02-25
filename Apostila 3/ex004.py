valores = [1,2,3,5,6,7,9]

def impar(x):
    return x % 2 != 0

print(list(filter(impar, valores)))