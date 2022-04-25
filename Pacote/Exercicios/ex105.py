def notas(*num, sit=False):
    """
    -> função para analizar notas e situações de varios alunos
    :param num: Valores das notas
    :param sit:(opcional) Mostrar ou não situação do aluno
    :return: Dicionario com a situação do aluno
    """
    aluno = dict()
    media = 0
    aluno['total'] = len(num)
    aluno['maior'] = max(num)
    aluno['menor'] = min(num)
    aluno['media'] = media = sum(num)/len(num)
    if sit:
        if media > 7:
            aluno['situacao'] = 'Boa'
        elif media > 4:
            aluno['situacao'] = 'Perigosa'
        else:
            aluno['situacao'] = 'Ruim'
    return aluno


dicionario = notas(5.6, 2, 4, 4, sit=False)
print(dicionario)
help(notas)