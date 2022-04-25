import math
ca1 = float(input('Digite o valor de um dos catetos:'))
ca2 = float(input('Digite o valor do outro cateto:'))
# hip = math.sqrt(math.pow(ca1, 2)+math.pow(ca2, 2))
hip = math.hypot(ca1, ca2)
print('A hipotenusa vai medir {:.2f}'.format(hip))
