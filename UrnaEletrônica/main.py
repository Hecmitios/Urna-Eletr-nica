from urna import *

candidato1 = Candidato(f'{vermelho}Lula{reset}', 'PT', 13, 0)
candidato2 = Candidato(f'{amarelo}Renan{reset}', 'Missão', 14, 0)
candidato3 = Candidato(f'{verde}Flávio{reset}', 'PL', 22, 0)
candidato4 = Candidato(f'{magenta}Pablo{reset}', 'PRTB', 28, 0)
candidato5 = Candidato(f'{cinza}Zema{reset}', 'Novo', 30, 0)
candidatoNulo = Candidato(f'{negrito}NULO{reset}', f'NENHUM', 00, 0)

listaCandidatos = [
                                candidato1,
                                candidato2,
                                candidato3,
                                candidato4,
                                candidato5,
                                candidatoNulo
                                ]


tabelaGeral(candidato1, candidato2, candidato3, candidato4, candidato5, candidatoNulo)


Urna.votar(candidato1, candidato2, candidato3, candidato4, candidato5, candidatoNulo)
Urna.apurar(listaCandidatos)




