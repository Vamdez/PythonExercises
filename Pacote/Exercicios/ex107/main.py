import moeda

num = float(input('Digite um valor:'))
print(f'O dobro de {num} é igual a {moeda.dobro(num):.2f}')
print(f'A metade de {num} é igual a {moeda.metade(num):.2f}')
print(f'Aumentando 13% de {num} é igual a {moeda.aumentar(num):.2f}')
print(f'Diminuindo 13% de {num} é igual a {moeda.diminuir(num):.2f}')
