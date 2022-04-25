from time import sleep
import escolhas


def Titulo():
    print(Linha('MENU PRINCIPAL', 3))


def header():
    print(Linha(
        f'1 - Ver pessoas cadastradas\n'
        f'2 - Cadastrar novas pessoas\n'
        f'3 - Sair do Sistema\n', 4))


def Menu():
    while True:
        sleep(0.3)
        Titulo()
        header()
        sleep(0.3)
        opc = leiaNum('Escolha uma opção: ')
        if opc == 1:
            escolhas.Escolha1()
        if opc == 2:
            escolhas.Escolha2()
        if opc == 3:
            escolhas.Escolha3()
            break


def Linha(msg=False, opc=0):
    print('-' * 30)
    if msg:
        return Cores(f'{msg: ^30}', opc)


def Cores(msg, opc=0):
    if opc == 1:  # Red
        return f'\33[31m{msg}\33[m'
    elif opc == 2:  # Green
        return f'\33[32m{msg}\33[m'
    elif opc == 3:  # Yellow
        return f'\33[33m{msg}\33[m'
    elif opc == 4:  # Blue
        return f'\33[34m{msg}\33[m'
    else:
        return f'{msg}'


def leiaNum(msg):
    valor = leiaInt(msg)
    while True:
        res = ValidationOpc(valor)
        if res:
            break
        print(Cores('Valor fora das opções!', 3))
        valor = leiaInt('Escolha uma opção: ')
    return valor


def leiaInt(msg):
    while True:
        try:
            valor = int(input(msg).strip())
        except (ValueError, TypeError):
            print(Cores('Digite um número inteiro', 1))
            continue
        return valor


def ValidationOpc(opc):
    return opc in range(1,4)
