n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1+n2)/2
if m < 4:
    print('Reprovado')
if 4 > m and 7 > m:
    print('Recuperação')
else :
    print('Aprovado')
