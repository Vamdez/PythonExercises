valores = []
maior = menor = 0
for c in range(5):
    if len(valores) > 0:
        v1 = int(input('Digite um valor:'))
        if v1 <= menor:
            menor = v1
        if v1 >= maior:
            maior = v1
        if len(valores) == 4:
            if v1 == menor:
                valores.insert(0, v1)
                print('Valor adicionada na posição 0')
            elif v1 == maior:
                valores.append(v1)
                print('Valor adicionado na última posição')
            elif v1 < valores[1]:
                valores.insert(1, v1)
                print('Valor adicionado na posição 1')
            elif v1 < valores[2]:
                valores.insert(2, v1)
                print('Valor adicionado na posição 2')
            else:
                valores.insert(3, v1)
                print('Valor adicionado na poisção 3')
        if len(valores) == 3:
            if v1 == menor:
                valores.insert(0, v1)
                print('Valor adicionada na posição 0')
            elif v1 == maior:
                valores.append(v1)
                print('Valor adicionado na última posição')
            elif v1 < valores[1]:
                valores.insert(1, v1)
                print('Valor adicionado na posição 1')
            else:
                valores.insert(2, v1)
                print('Valor adicionado na posição 2')
        if len(valores) == 2:
            if v1 == menor:
                valores.insert(0, v1)
                print('Valor adicionada na posição 0')
            elif v1 == maior:
                valores.append(v1)
                print('Valor adicionado na última posição')
            else:
                valores.insert(1, v1)
                print('Valor adicionado na posição 1')
        if len(valores) == 1:
            if v1 <= valores[0]:
                 valores.insert(0, v1)
                 print('Valor adicionado na posição 0')
            elif v1 > valores[0]:
                valores.insert(1, v1)
                print('Valor adicionado na posição 1')
    else:
        valores.append(int(input('Digite um valor:')))
        print('Valor adicionado na posição 0')
        maior = menor = valores[0]
print('=-'*20)
print(f'Os valores adicionados são {valores}')
