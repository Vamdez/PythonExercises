casa = int(input('Digite o valor da casa:'))
salar = float(input('Digite o seu salario:'))
meses = int(input('Em quantos anos pretende comprar essa casa?'))*12
prest = casa/meses
print('O valor da prestação mensal é igual a \33[34m R${:.2f} \33[0m'.format(prest))
if prest > (salar*30)/100:
    print('O emprestimo foi negado')
else:
    print('O esprestimo foi aprovado')
