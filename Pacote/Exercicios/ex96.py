def area(lar, comp):
    ar = lar * comp
    print(f'A área do terreno ({lar} x {comp}) e de {ar}m²')


largura = float(input('Digite a largura: '))
comprimento = float(input('Digite o comprimento: '))
area(largura, comprimento)
