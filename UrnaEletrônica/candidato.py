from cores import *
class Candidato:

    def __init__(self, nome, partido, numero, quantVotos,):
        self.nome = nome
        self.partido = partido
        self.numero = numero
        self.quantVotos = quantVotos
    def exibirCandidato(self):
        return ' {}  |   {}   |  {} '.format(self.nome, self.partido, self.numero)
    