from colorama import Fore, Back, Style
class Kandidato:

    def __init__(self, nome, partido, numero):
        self.nome = nome
        self.partido = partido
        self.numero = numero

    def tabelakandidato():
        return(' Nome   Partido  Número')
    def exibirkandidato(self):
        return ' {}  |   {}   |  {} '.format(self.nome, self.partido, self.numero)

kandidato1 = Kandidato('Lula', 'PT', 13)
kandidato2 = Kandidato('Renan', 'Missão', 14)
kandidato3 = Kandidato('Flávio', 'PL', 22)
kandidato4 = Kandidato('Pablo', 'PRTB', 28)
kandidato5 = Kandidato('Romeu', 'Novo', 30)

print(Kandidato.tabelakandidato())
print(kandidato1.exibirkandidato())
print(kandidato2.exibirkandidato())
print(kandidato3.exibirkandidato())
print(kandidato4.exibirkandidato())
print(kandidato5.exibirkandidato())

