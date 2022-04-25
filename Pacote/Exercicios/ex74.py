from random import randint
#numeros = (randint(0, 10), randint(0, 10), randint(0, 10),
 #          randint(0, 10), randint(0, 10),)
numeros = tuple(randint(1, 1000) for i in range(1000))
print(numeros)
print(max(numeros))
print(min(numeros))
print('Fim')