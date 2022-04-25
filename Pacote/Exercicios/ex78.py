valores = list()
pmenor = list()
pmaior = list()
menor = maior = 0
for c in range(0, 5):
    valores.append(int(input(f'Digite o número da posição {c}:')))
    if valores[c] < menor or menor == 0:
        menor = valores[c]
    elif valores[c] > maior or maior ==0:
        maior = valores[c]
    if c == 4:
        for i in range(0, 5):
            if valores[i] == menor:
                pmenor.append(i)
            if valores[i] == maior:
                pmaior.append(i)
print('=-'*20)
print(f'Você digitou os valores: {valores}')
print(f'O menor valor digitado foi {menor}, na posição {pmenor}')
print(f'O maior valor digitado foi {maior}, na posição {pmaior}')

