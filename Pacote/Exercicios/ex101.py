from datetime import date


def voto(nasc):
    idade = date.today().year - nasc
    print(f'Com {idade} anos:', end=' ')
    if idade < 16:
        return 'NÃO VOTA'
    elif idade < 18:
        return 'VOTO OPCIONAL'
    elif idade < 65:
        return 'VOTO OBRIGATORIO'
    else:
        return 'VOTO OPCIONAL'


resposta = voto(int(input('Que ano você nasceu? ')))
print(resposta)
