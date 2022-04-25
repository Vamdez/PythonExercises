
class Pessoa:
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def falar(self, msg):
        msg = f'\33[34m{msg}\33[m'

        if self.comendo:
            print(f'{self.nome} não pode falar comendo')
            return

        if self.falando:
            print(f'{self.nome} já está falando')
            return

        print(f'{self.nome} está falando: {msg}')
        self.falando = True

    def parar_de_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando')
            return

        print(f'{self.nome} parou de falar')
        self.falando = False

    def comer(self, alimento):
        if self.falando:
            print(f'{self.nome} não pode comer falando')
            return

        if self.comendo:
            print(f'{self.nome} já está comendo')
            return

        print(f'{self.nome} está comendo {alimento}')
        self.comendo = True

    def parar_de_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo')
            return

        print(f'{self.nome} parou de comer')
        self.comendo = False