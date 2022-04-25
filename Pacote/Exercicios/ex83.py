exp = list(str(input('Digite uma expressão: ')))
abre = exp.index('(')
fecha = exp.index(')')
a = f = c = 0
invalida = 0
while c < len(exp):
    if exp[c] == '(':
        a += 1
    elif exp[c] == ')':
        f += 1
    c += 1
    if f > a:
        invalida = 1
        break
if fecha < abre:
    print('Sua expressão é invalida1')
elif exp.count('(') != exp.count(')'):
    print('Sua expressão é invalida2')
elif invalida == 1:
    print('Sua expressão é invalida3')
else:
    print('Sua expressão é válida')


