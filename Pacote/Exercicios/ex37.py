num = int(input('Digite um numero inteiro: '))
print('[1] Converter de decimal para \33[34m BINARIO\33[m \n'
      '[2] Converter de decimal para \33[34m OCTAL \33[m \n'
      '[3] Converter de decimal para \33[34m HEXADECIMAL\33[m \n')
opcao = int(input('Digite sua opção:'))
if opcao == 1:
    a = format(num, 'b')
    print('O valor {} em binario é igual a {}'.format(num, a))
elif opcao == 2:
    a = format(num, 'o')
    print('O valor {} em octal é igual a {}'.format(num, a))
elif opcao == 3:
    a = format(num, 'x')
    print('O valor {} em hexadecimal é igual a {}'.format(num, a))
else:
    print('Opção nao valida')
