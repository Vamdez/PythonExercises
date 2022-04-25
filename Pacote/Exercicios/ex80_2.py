lista = list()
for c in range(5):
    n = int(input("Digite o numero: "))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Valor adicionado na última posição')
    else:
        for pos, x in enumerate(lista):
            if n <= x:
                lista.insert(pos, n)
                print(f'Valor adicionado na posição {pos}')
                break
print(lista)