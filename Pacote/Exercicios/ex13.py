sal = float(input('Digite o salário do funcionario: R$'))
upper = sal + (sal*15/100)
print('Um funcionario que recebia R${}, com o reajuste de 15% vai passar a receber R${:.2f}'.format(sal, upper))
