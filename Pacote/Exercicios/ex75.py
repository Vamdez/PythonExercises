
numeros = tuple(int(input('Digite um número:')) for i in range(4))
print(f'Você digitou os valores: {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3) + 1}° posição')
else:
    print(f'O valor 3 não apareceu')
print('Os valores pares digitados são:', end='')
for c in range(4):
    if numeros[c] % 2 == 0:
        print(numeros[c], end='')
