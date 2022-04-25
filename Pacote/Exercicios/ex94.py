cadastros = list()
pessoas = dict()
total = count = 0
while True:
    opc = ' '
    pessoas.clear()
    pessoas['nome'] = str(input('Nome:'))
    while opc not in 'MF':
        pessoas['sexo'] = opc = str(input('Sexo[M/F]:')).upper().strip()
    pessoas['idade'] = int(input('Idade:'))
    cadastros.append(pessoas.copy())
    total += pessoas['idade']
    while opc not in 'SN':
        opc = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if opc == 'N':
        break
media = total/len(cadastros)
print(f'AO TODO FORAM CADASTRADOS {len(cadastros)} pessoas')
print(f'A média de idade é de {media:.2f}')
print(f'As mulheres cadastradas foram >>', end=' ')
for c in range(len(cadastros)):
    if cadastros[c]['sexo'] == 'F':
        print({cadastros[c]["nome"]}, end=' ')
print('\nLista de pessoas que estão acima da média:',end='')
for c in range(len(cadastros)):
    if cadastros[c]['idade'] >= media:
        print('\n')
        print('='*30)
        for k, v in cadastros[c].items():
            print(f'{k} = {v}', end=';')
