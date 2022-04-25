v1 = input('Digite Algo:')
print('O tipo primitivo desse valor é {} \n'.format(type(v1)),
      'Só tem espaço? {}\n'.format(v1.isspace()),
      'É um número? {}\n'.format(v1.isnumeric()),
      'É alfabeto? {}\n'.format(v1.isalpha()),
      'É alfanumérico? {}\n'.format(v1.isalnum()),
      'Está em maiúscula? {}\n'.format(v1.isupper()),
      'Está em minusculo? {}\n'.format(v1.islower()),
      'Está capitalizada? {}\n'.format(v1.istitle()))


