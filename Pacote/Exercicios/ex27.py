nome = str(input('Digite Seu Nome Completo: ')).strip()
y = nome.split()
print('O seu primeiro nome é {}'.format(y[0]))
print('O seu último nome é {}'.format(y[len(y)-1]))
