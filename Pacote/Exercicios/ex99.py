def maiornum(*num):
    maior = 0
    for c in range(len(num)):
        if num[c] > maior or maior == 0:
            maior = num[c]
    print(f'Analisando os valores passados...\n'
          f'{num} Foram informados {len(num)} valores\n'
          f'O maior valor informado foi {maior}')


maiornum(10, 4, 5, 12, 0)
maiornum(2, 9, 7, 4, 5)
maiornum()