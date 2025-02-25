from functools import reduce

valores = [4,6,8]

def soma (a,b):
    return a + b

print(reduce(soma,valores))