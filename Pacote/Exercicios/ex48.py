total = 0
num = 0
for c in range(1,501,2):
    if c % 3 == 0:
        total = total + c
        num = num + 1
print('A soma de todos os numeros multiplos de 3 impares entre 1 e 500 é igual a: {}'.format(total))
print(num)
