from time import sleep
c = ['\33[97;41m',   #Vermelho
     '\33[97;46m',   #Ciano
     '\33[30;107m',  #Branco
     '\33[30;102m'   #Verde
     ]


def linha(msg, cor=0):
    print(f'{c[cor]}~'*(len(msg)+4))
    print(f'  {msg}')
    print('~'*(len(msg)+4))
    print('\33[m')


opc = ''
while True:
    linha('SISTEMA DE AJUDA PyHelp', 1)
    opc = str(input('Função ou biblioteca: ')).strip()
    if opc.upper() == 'FIM':
        linha('Até logo')
        break
    linha(f'Acessando o manual do comando {opc}', 2)
    sleep(0.5)
    print(f'{c[3]}')
    help(opc)

