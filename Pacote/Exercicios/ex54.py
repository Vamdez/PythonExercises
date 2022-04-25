menor = 0
maior = 0
for c in range(1, 8):
    s = int(input(f'Digite o ano de nascimento da {c}° pessoa:'))
    if s >=2004:
        menor = menor + 1
    else:
        maior = maior + 1
print(f'Ao todo tivemos {maior} pessoas maiores de idade')
print(f'E tambem {menor} pessoas menores de idade')


