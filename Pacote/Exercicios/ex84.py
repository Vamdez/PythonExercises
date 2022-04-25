nomes = list()
dados = list()
menor = maior = 0
while True:
    opc = ' '
    nomes.append(str(input('Digite seu nome:')).title())
    nomes.append(float(input('Digite seu peso: ')))
    if nomes[1] < menor or menor == 0:
        menor = nomes[1]
    if nomes[1] > maior or maior == 0:
        maior = nomes[1]
    while opc not in 'SN':
        opc = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    dados.append(nomes[:])
    nomes.clear()
    if opc == 'N':
        break
print(f'Ao todo você cadastrou {len(dados)} pessoas')
print(f'O menor peso foi de {menor} Kg. Peso de', end=' ')
for c in range(len(dados)):
    if dados[c][1] == menor:
        print(dados[c][0], end=' ')
print(f'\nO maior peso foi de {maior} Kg. Peso de', end =' ')
for c in range(len(dados)):
    if dados[c][1] == maior:
        print(dados[c][0], end=' ')