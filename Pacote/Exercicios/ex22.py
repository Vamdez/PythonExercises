nome = str(input('Digite seu nome Completo:'))
upper = nome.upper()
lower = nome.lower()
nletras = (len(nome)) - (nome.count(' '))
divisao = nome.split()
print('Analizando seu nome.........')
print('Seu nome em maiusculo é {}.\n'.format(upper),
      'Seu nome em minusculo é {}.\n'.format(lower),
      'Seu nome tem ao todo {} letras.\n'.format(nletras),
      'Seu primeiro nome é {} e tem {} letras.'.format(divisao[0], len(divisao[0])))

