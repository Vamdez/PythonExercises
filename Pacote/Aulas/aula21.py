def fator(num = 1):
    f1 = 1
    for c in range(num, 0, -1):
        f1 = f1 * c
    return f1


resul1 = fator(5)
resul2 = fator(15)
resul3 = fator(9)
resul4 = fator(int(input('Digite um numero: ')))
print(f'Os resultados foram, {resul1}, {resul2}, {resul3}, {resul4}')