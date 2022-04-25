salario = float(input('Digite o seu salário: '))
if salario < 1250:
    final = salario + salario*(15/100)
else:
    final = salario + salario*(1/10)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(salario, final))
