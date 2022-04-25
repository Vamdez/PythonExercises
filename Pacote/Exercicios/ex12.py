v1 = float(input('Qual o preço do produto: R$ '))
desc = v1 - (v1 * (5/100))
print('O produto que custa R${}, na promoção de 5% vai passar a custa {:.2f}'.format(v1, desc))
