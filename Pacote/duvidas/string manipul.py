lista = ['auto', 'didactic', 'graph', 'mate', 'chrome', 'centric', 'complete',
              'echolalia', 'encoder', 'biography']


def tudo(vocab_words):
    palavra = vocab_words[0] + ':'
    for c in range(1, len(vocab_words)):
        if c == len(vocab_words) - 1:
            palavra += f': {vocab_words[0] + vocab_words[c]}'
        else:
            palavra += f': {vocab_words[0] + vocab_words[c]} :'
    return palavra


x = tudo(lista)
print(x)
