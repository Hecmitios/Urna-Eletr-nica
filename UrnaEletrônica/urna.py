from cores import *
class Candidatos:

    def __init__(self, nome, partido, numero, votos):
        self.nome = nome
        self.partido = partido
        self.numero = numero
        self.quantVotos = votos

    def topoTabela():
        return(' Nome   Partido  Número')
    
    def exibirCandidato(self):
        return ' {}  |   {}   |  {} '.format(self.nome, self.partido, self.numero)

    def tabelaGeral(self):
        print(Candidatos.topoTabela())
        print(candidato1.exibirCandidato())
        print(candidato2.exibirCandidato())
        print(candidato3.exibirCandidato())
        print(candidato4.exibirCandidato())
        print(candidato5.exibirCandidato())

    def votar(self):
        print(f'Muito bem, eleitor, agora você deve votar, pois nesse país, todos são obrigados a tal')
        print('')

candidato1 = Candidatos('Lula', 'PT', 13, 0)
candidato2 = Candidatos('Renan', 'Missão', 14, 0)
candidato3 = Candidatos('Flávio', 'PL', 22, 0)
candidato4 = Candidatos('Pablo', 'PRTB', 28, 0)
candidato5 = Candidatos('Romeu', 'Novo', 30, 0)




if __name__ == '__main__':

    Candidatos.tabelaGeral()

    ''''print(Candidatos.topoTabela())
    print(candidato1.exibirCandidato())
    print(candidato2.exibirCandidato())
    print(candidato3.exibirCandidato())
    print(candidato4.exibirCandidato())
    print(candidato5.exibirCandidato())'''



