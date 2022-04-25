valores = []
par = []
impar = []
while True:
    opc = ' '
    valores.append(int(input('Digite um valor:')))
    while opc not in 'SN':
        opc = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if opc == 'N':
        break
for c in range(len(valores)):
    if valores[c] % 2 == 0:
        par.append(valores[c])
    else:
        impar.append((valores[c]))
print(par)
print(impar)
print(valores)
