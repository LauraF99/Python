lista = [1,2,3,4,5,6,7,8,9,10]

for i in lista:
    if i == 5:
        break
    print(i)

for i in lista:
    if i == 5:
        continue
    print(i)

for i in lista:
    if i == 5:
        pass
    print(i)