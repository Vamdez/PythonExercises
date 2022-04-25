menor = 0
maior = 0
for c in range(1, 6):
    peso = float(input(f'Peso da {c}° pessoa:'))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if maior <= peso:
            maior = peso
        elif menor >= peso:
            menor = peso
print(f'Maior é igual a {maior}, Menor é igual a {menor}')

