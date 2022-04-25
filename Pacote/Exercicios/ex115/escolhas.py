import utils

def Escolha1():
    print(utils.Linha('Pessoas Cadastradas'))
    utils.Linha()
    ExisteArqui()
    arquivo = open('lista.txt', 'r')
    for itens in arquivo.readlines():
        print(itens, end='')
    arquivo.close()


def Escolha2():
    print(utils.Linha('Cadastrando novas Pessoas'))
    utils.Linha()
    arquivo = open('lista.txt', 'a')
    try:
        name = str(input('Digite o nome: '))
    except(ValueError, KeyboardInterrupt):
        name = '<desconhecido>'
        print()
    years = utils.leiaInt('Digite a idade:')
    arquivo.write(f'{name:<20} {years:>2} Anos \n')
    arquivo.close()


def Escolha3():
    print(utils.Linha('Finalizando programa, até a proxima...', 3))


def ExisteArqui():
    try:
        a = open('lista.txt', 'r')
        a.close()
    except FileNotFoundError:
        a = open('lista.txt', 'w+')
        a.close()
