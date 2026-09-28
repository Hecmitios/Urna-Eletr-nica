class Candidato:

    def __init__(self, nome, partido, numero, quantVotos,):
        self.nome = nome
        self.partido = partido
        self.numero = numero
        self.quantVotos = quantVotos
        
    def exibirCandidato(self):
        return ' {}  |   {}   |  {} '.format(self.nome, self.partido, self.numero)

candidato1 = Candidato('Lula', 'PT', 13, 0)
candidato2 = Candidato('Renan', 'Missão', 14, 0)
candidato3 = Candidato('Flávio', 'PL', 22, 0)
candidato4 = Candidato('Pablo', 'PRTB', 28, 0)
candidato5 = Candidato('Zema', 'Novo', 30, 0)
candidatoNulo = Candidato('NULO', 'NENHUM', 00, 0)

listaCandidatos = [
                                candidato1,
                                candidato2,
                                candidato3,
                                candidato4,
                                candidato5,
                                candidatoNulo
                                ]