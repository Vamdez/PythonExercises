opc = 's'
count = maior = soma = menor = 0
while opc == 's':
    v1 = int(input('Digite um número:'))
    opc = str(input('Deseja continuar?[s/n]')).strip().lower()
    count += 1
    soma += v1
    if maior == 0 or v1 > maior:
        maior = v1
    if menor == 0 or v1 < menor:
        menor = v1
print(f'Você digitou {count} numeros, e a média foi {soma/count}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
print('Fim')