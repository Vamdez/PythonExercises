print('+-+_+'*5)
print('ANALIZADOR DE TRIANGULOS')
print('+-+_+'*5)
v1 = float(input('Digite o valor do primeiro lado do triangulo: '))
v2 = float(input('Digite o valor do segundo lado do triangulo: '))
v3 = float(input('Digite o valor do terceiro lado do triangulo: '))
if v1+v2 <= v3 or v2+v3 <= v1 or v1+v3 <=v2:
    print('Os segmentos acima NÃO PODEM formar um triangulo')
else:
    print('Os segmentos acima PODEM formar um triangulo')