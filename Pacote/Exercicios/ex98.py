from time import sleep


def contador(a, b, c):
    for v in range(a, b, c):
        print(v, end=' ')
        sleep(0.3)
    print('Fim!')


def lin():
    print('=-'*20)


lin()
print('Contagem de 1 a 10 de 1 em 1')
contador(0, 11, 1)
lin()
print('Contagem de 10 a 0 de 2 em 2')
contador(10, -1, -2)
lin()
print('Agora é sua vez de personalizar:')
inicio = int(input('Inicio:'))
fim = int(input('Fim:'))
passo = int(input('Passo:'))
if passo == 0:
    passo = 1
if fim < inicio and passo > 0:
    contador(inicio, fim-1, -passo)
elif passo < 0:
    contador(inicio, fim-1, passo)
else:
    contador(inicio, fim+1, passo)
