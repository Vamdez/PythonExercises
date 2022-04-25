v1 = int(input('Digite um numero:'))
v2 = int(input('Digite outro numero:'))
s = v1+v2
m = v1*v2
d = v1/v2
p = v1**v2

print('A soma é igual a {} \n'
      'A multiplicação é igual a {} \n'
      'A divisão é igual a {:.5f} \n'
      'A potenciação é igual a {}'.format(s, m, d, p))
