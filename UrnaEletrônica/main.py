from urna import *

candidato1 = Candidatos('Lula', 'PT', 13, 0)
candidato2 = Candidatos('Renan', 'Missão', 14, 0)
candidato3 = Candidatos('Flávio', 'PL', 22, 0)
candidato4 = Candidatos('Pablo', 'PRTB', 28, 0)
candidato5 = Candidatos('Romeu', 'Novo', 30, 0)
candidatoNulo = Candidatos('NULO', 'NENHUM', 00, 0)


tabelaGeral(candidato1, candidato2, candidato3, candidato4, candidato5, candidatoNulo)

Candidatos.votar(candidato1, candidato2, candidato3, candidato4, candidato5, candidatoNulo)




