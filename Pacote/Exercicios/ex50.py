total = 0
for c in range(1, 7):
    v1 = int(input(f'Digite o valor do {c}° numero:'))
    if v1 % 2 == 0:
        total += v1
print(f'A soma de todos os numeros pares é igual a {total}')
