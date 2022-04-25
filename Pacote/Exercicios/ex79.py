lista = []
while True:
    opc = ' '
    v1 = int(input('Digite um valor:'))
    if v1 not in lista:
        lista.append(v1)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    while opc not in 'SN':
        opc = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if opc == 'N':
        break
print('=>'*20)
print(f'Os valores digitados foram {sorted(lista)}')
