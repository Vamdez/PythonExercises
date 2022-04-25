notas = []
temp = []
while True:
    opc = ' '
    temp.append(str(input('Nome:').title()))
    temp.append(float(input('Nota 1: ')))
    temp.append(float(input('Nota 2: ')))
    temp.append((temp[1] + temp[2])/2)
    notas.append(temp[:])
    temp.clear()
    while opc not in 'SN':
        opc = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if opc == 'N':
        break
print('-='*30)
print('No. Nome         Média')
print('-'*22)
for c in range(len(notas)):
    print(c, end='  ')
    print(f'{notas[c][0]:<10}', end=' '*5)
    print(f'{notas[c][3]:>4.2f}')
while True:
    v1 = int(input('Mostrar notas de qual aluno? (999 interrompe)'))
    if v1 == 999:
        break
    print(f'Notas de {notas[v1][0]} são {notas[v1][1]} e {notas[v1][2]}')
print('-='*30)
print('Obrigado por usar nosso serviço')
