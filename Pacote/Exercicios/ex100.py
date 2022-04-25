from random import randint


def somaPar(lista):
    soma = 0
    print(f'Somando os valores pares de {lista}', end=' ')
    for c in range(5):
        if lista[c] % 2 == 0:
            soma += lista[c]
    print(f'Temos {soma}')


def randomlist():
    print('Sorteando 5 valores da lista:,', end=' ')
    sorteio = list()
    for c in range(5):
        sorteio.append(randint(0, 10))
    print(sorteio)
    return sorteio


aleatorio = randomlist()
somaPar(aleatorio)

