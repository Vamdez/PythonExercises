valores = list()
decrescente = list()
while True:
    opc = ' '
    v1 = int(input('Digite um valor:'))
    valores.append(v1)
    while opc not in 'SN':
        opc = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if opc == 'N':
        break
print('=='*10)
print(f'Foram digitados {len(valores)} valores')
valores.sort(reverse=True)
print(valores)
if 5 in valores:
    print('O valor 5 faz parte da lista')
else:
    print('O valor 5 não faz parte da lista')

