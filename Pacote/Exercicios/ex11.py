largura = float(input('Digite a largura da parede:'))
altura = float(input('Digite o altura da parede:'))
area = largura * altura
litro = area/2
print('Sua parede tem a dimensão de {} x {} e sua área é igual {}m².'.format(largura, altura, area))
print('Para pintar essa parede, você precisará de {:.2}l de tinta.'.format(litro))