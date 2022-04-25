homem = total18 = mulher20 = 0
opc = ''

while True:
    opc = ' '
    sexo = ' '
    print('-=' * 10)
    print('CADASTRE UMA PESSOA')
    print('-='*10)
    idade = int(input('Idade: '))
    while sexo not in 'MF':
        sexo = str(input('Sexo:[M/F]')).strip().upper()
    if sexo == 'M':
        if idade > 18:
            total18 += 1
        homem += 1
    if sexo == 'F':
        if idade > 20:
            total18 += 1
        elif idade < 18:
            mulher20 += 1
        else:
            mulher20 += 1
            total18 += 1
    while opc not in 'SN':
        opc = str(input('Deseja continuar? [S/N]')).strip().upper()
    if opc == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {total18}')
print(f'Ao todo temos {homem} homens cadastrados')
print(f'E temos {mulher20} mulher com menos de 20 anos')