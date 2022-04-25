import moeda_2

num = float(input('Digite o preço:'))
print(f'O dobro de {moeda_2.moeda(num)} é igual a {moeda_2.dobro(num)}')
print(f'A metade de {moeda_2.moeda(num)} é igual a {moeda_2.metade(num)}')
print(f'Aumentando 13% de {moeda_2.moeda(num)} é igual a {moeda_2.aumentar(num, 13)}')
print(f'Diminuindo 15% de {moeda_2.moeda(num)} é igual a {moeda_2.diminuir(num, 15)}')