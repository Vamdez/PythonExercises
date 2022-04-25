v = int(input('Digite um numero pra calcular o fatorial: '))
print(f'Calculando {v}! =', end=' ')
total = 1
while v != 1:
    print(v,'x', end=' ')

    total = v * total
    v -= 1
print(f'1\nO resultado é igual a {total}')