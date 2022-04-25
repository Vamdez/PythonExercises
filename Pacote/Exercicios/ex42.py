l1 = float(input('Primeiro lado do triangulo: '))
l2 = float(input('Segundo lado do triangulo: '))
l3 = float(input('Terceiro lado do triangulo: '))
if l1+l2 <= l3 or l2+l3 <= l1 or l1+l3 <=l2:
    print('Os segmentos acima NÃO PODEM formar um triangulo')
elif l1!= l2 and l2 != l3 and l1 != l3:
    print('Os segmentos acima podem formar um triango ESCALENO')
elif l1 == l2 == l3:
    print('Os segmentos acima podem formar um triangulo EQUILATERO')
else:
    print('Os segmentos acima podem formar um triangulo ISOSCELES')

