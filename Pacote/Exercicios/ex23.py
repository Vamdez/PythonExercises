num = int(input('Digite um numero: ').strip())
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10


print('Analizando o numero {} \n'.format(num),
      'Unidade {} \n'.format(u),
     'Dezena {} \n'.format(d),
      'Centena {} \n'.format(c),
      'Milhar {}'.format(m))
