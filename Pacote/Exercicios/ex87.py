matriz = [[], [], []]
soma = somacol = 0
for l in range(3):
    for c in range(3):
        v1 = int(input(f'Digite o valor de posição [{l}][{c}]:'))
        if v1 % 2 == 0:
            soma += v1
        if c == 2:
            somacol += v1
        matriz[l].append(v1)
for l in range(3):
    for c in range(3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print('\n')
print(f'A soma dos valores pares é igual a: {soma}')
print(f'A soma dos valores da terceira coluna é iguala a: {somacol}')
print(f'O maior valor da segunda linha é: {max(matriz[1])}')
