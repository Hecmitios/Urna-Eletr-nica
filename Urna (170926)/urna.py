from cores import *
class Candidato:

    def __init__(self, nome, partido, numero):
        self.nome = nome
        self.partido = partido
        self.numero = numero

    def tabelaCandidato():
        return(' Nome   Partido  Número')
    
    def exibirCandidato(self):
        return ' {}  |   {}   |  {} '.format(self.nome, self.partido, self.numero)

    def votar(self):
        print(f'Muito bem, eleitor, agora você deve votar, pois nesse país, todos são obrigados a tal')

candidato1 = Candidato('Lula', 'PT', 13)
candidato2 = Candidato('Renan', 'Missão', 14)
candidato3 = Candidato('Flávio', 'PL', 22)
candidato4 = Candidato('Pablo', 'PRTB', 28)
candidato5 = Candidato('Romeu', 'Novo', 30)



