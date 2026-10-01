class Candidato: 

    def __init__(self, nome, partido, numero, quantVotos, imagem):
        self.nome = nome
        self.partido = partido
        self.numero = numero
        self.quantVotos = quantVotos
        self.imagem = imagem

candidato1 = Candidato('Lula', 'PT', '13', 0, 'imagens/lula.png')
candidato2 = Candidato('Renan', 'Missão', '14', 0, 'imagens/renan.png')
candidato3 = Candidato('Flávio', 'PL', '22', 0, 'imagens/flavio.png')
candidato4 = Candidato('Pablo', 'PRTB', '28', 0, 'imagens/marcal.png')
candidato5 = Candidato('Zema', 'Novo', '30', 0, 'imagens/zema.png')
candidato6 = Candidato('Cury', 'AVANTE', '70', 0, 'imagens/cury.png')
candidato7 = Candidato('Samara', 'UP', '80', 0, 'imagens/samara.png')
candidatoNulo = Candidato('NULO', 'NENHUM', '00', 0, 'imagens/nulo.png')

listaCandidatos = [
                                candidato1,
                                candidato2,
                                candidato3,
                                candidato4,
                                candidato5,
                                candidato6,
                                candidato7,

                                candidatoNulo
                                ]